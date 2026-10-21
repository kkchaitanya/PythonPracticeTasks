import os
from neo4j import GraphDatabase

# --------------------------------------------------
# Configuration & Credentials
# --------------------------------------------------
NEO4J_URI = os.getenv("NEO4J_URI", "neo4j+s://93dd8a27.databases.neo4j.io")
NEO4J_USERNAME = os.getenv("NEO4J_USERNAME", "93dd8a27")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD", "wZ6NKZmk6a5DZz23oavRAoelrjNJ2LfTy1mAYfEH6tI")

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)


def run_query(query: str, parameters: dict | None = None) -> list[dict]:
    """Execute a single Cypher query and return results as a list of dicts."""
    with driver.session() as session:
        result = session.run(query, parameters or {})
        return [record.data() for record in result]


# --------------------------------------------------
# Database Setup
# --------------------------------------------------
CLEAR_DATABASE = """
MATCH (n) DETACH DELETE n
"""

CREATE_NODES = """
CREATE
  // Countries
  (c1:Country {name: 'USA'}),
  (c2:Country {name: 'China'}),
  (c3:Country {name: 'India'}),
  (c4:Country {name: 'Germany'}),

  // Suppliers
  (s1:Supplier {supplierId: 'S1', name: 'Supplier A', tier: 1}),
  (s2:Supplier {supplierId: 'S2', name: 'Supplier B', tier: 1}),
  (s3:Supplier {supplierId: 'S3', name: 'Supplier C', tier: 2}),
  (s4:Supplier {supplierId: 'S4', name: 'Supplier D', tier: 2}),

  // Components
  (cm1:Component {componentId: 'C1', name: 'Processor'}),
  (cm2:Component {componentId: 'C2', name: 'Battery'}),
  (cm3:Component {componentId: 'C3', name: 'Display'}),
  (cm4:Component {componentId: 'C4', name: 'Lithium Cell'}),

  // Products
  (p1:Product {productId: 'P1', name: 'Smartphone'}),
  (p2:Product {productId: 'P2', name: 'Tablet'}),
  (p3:Product {productId: 'P3', name: 'Laptop'}),

  // Plants
  (pl1:Plant {plantId: 'PL1', name: 'Hyderabad Plant'}),
  (pl2:Plant {plantId: 'PL2', name: 'Singapore Plant'}),
  (pl3:Plant {plantId: 'PL3', name: 'Berlin Plant'}),

  // Shipments
  (sh1:Shipment {shipmentId: 'SH1'}),
  (sh2:Shipment {shipmentId: 'SH2'})
"""

CREATE_RELATIONSHIPS = """
MATCH
  (s1:Supplier {name: 'Supplier A'}),
  (s2:Supplier {name: 'Supplier B'}),
  (s3:Supplier {name: 'Supplier C'}),
  (s4:Supplier {name: 'Supplier D'}),

  (cm1:Component {name: 'Processor'}),
  (cm2:Component {name: 'Battery'}),
  (cm3:Component {name: 'Display'}),
  (cm4:Component {name: 'Lithium Cell'}),

  (p1:Product {name: 'Smartphone'}),
  (p2:Product {name: 'Tablet'}),
  (p3:Product {name: 'Laptop'}),

  (pl1:Plant {name: 'Hyderabad Plant'}),
  (pl2:Plant {name: 'Singapore Plant'}),
  (pl3:Plant {name: 'Berlin Plant'}),

  (c1:Country {name: 'USA'}),
  (c2:Country {name: 'China'}),
  (c3:Country {name: 'India'}),
  (c4:Country {name: 'Germany'}),

  (sh1:Shipment {shipmentId: 'SH1'}),
  (sh2:Shipment {shipmentId: 'SH2'})

CREATE
  // Supplier Locations
  (s1)-[:LOCATED_IN]->(c1),
  (s2)-[:LOCATED_IN]->(c2),
  (s3)-[:LOCATED_IN]->(c3),
  (s4)-[:LOCATED_IN]->(c4),

  // Supplier-to-Supplier Tier Relationships
  (s3)-[:SUPPLIES_TO]->(s1),
  (s4)-[:SUPPLIES_TO]->(s2),

  // Component Supplies
  (s1)-[:SUPPLIES]->(cm1),
  (s1)-[:SUPPLIES]->(cm2),
  (s2)-[:SUPPLIES]->(cm3),
  (s3)-[:SUPPLIES]->(cm4),

  // Component Usage in Products
  (cm1)-[:USED_IN]->(p1),
  (cm1)-[:USED_IN]->(p2),
  (cm2)-[:USED_IN]->(p1),
  (cm3)-[:USED_IN]->(p2),
  (cm3)-[:USED_IN]->(p3),
  (cm4)-[:USED_IN]->(p1),

  // Manufacturing Locations
  (p1)-[:MANUFACTURED_AT]->(pl1),
  (p2)-[:MANUFACTURED_AT]->(pl2),
  (p3)-[:MANUFACTURED_AT]->(pl3),

  // Shipments
  (sh1)-[:CONTAINS]->(cm1),
  (sh1)-[:DESTINED_FOR]->(pl1),
  (sh2)-[:CONTAINS]->(cm3),
  (sh2)-[:DESTINED_FOR]->(pl3)
"""

# --------------------------------------------------
# 11 Cypher Traversal & Analytical Queries
# --------------------------------------------------

# 1. Single-Hop: Direct Component Supply
QUERY_1 = """
MATCH (s:Supplier {name: 'Supplier A'})-[:SUPPLIES]->(c:Component)
RETURN s.name AS Supplier, c.name AS Component
"""

# 2. Multi-Hop: Supplier -> Component -> Product -> Plant
QUERY_2 = """
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant)
RETURN s.name AS Supplier,
       c.name AS Component,
       p.name AS Product,
       pl.name AS Plant
"""

# 3. Property Filtering: Tier-1 Suppliers in target countries
QUERY_3 = """
MATCH (c:Country)<-[:LOCATED_IN]-(s:Supplier)
WHERE s.tier = 1 AND c.name IN ['USA', 'China']
RETURN s.supplierId AS SupplierID,
       s.name AS SupplierName,
       c.name AS Country
"""

# 4. Inbound / Upstream Traversal: Plant Impact Analysis
QUERY_4 = """
MATCH (pl:Plant {name: 'Hyderabad Plant'})<-[:MANUFACTURED_AT]-(p:Product)<-[:USED_IN]-(c:Component)<-[:SUPPLIES]-(s:Supplier)
RETURN DISTINCT
       pl.name AS Plant,
       p.name AS AffectedProduct,
       c.name AS RequiredComponent,
       s.name AS UpstreamSupplier
"""

# 5. Multi-Hop Undirected / Destination Matching: Shipment verification
QUERY_5 = """
MATCH (sh:Shipment)-[:CONTAINS]->(c:Component)-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant)
WHERE (sh)-[:DESTINED_FOR]->(pl)
RETURN sh.shipmentId AS Shipment,
       c.name AS Component,
       p.name AS Product,
       pl.name AS DestinationPlant
"""

# 6. Aggregation & Counting: Components per product
QUERY_6 = """
MATCH (c:Component)-[:USED_IN]->(p:Product)
RETURN p.name AS Product,
       count(DISTINCT c) AS TotalComponentsUsed,
       collect(c.name) AS ComponentList
ORDER BY TotalComponentsUsed DESC
"""

# 7. Aggregation with Filtering: Critical suppliers serving multiple products
QUERY_7 = """
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)
WITH s, count(DISTINCT p) AS ProductCount, collect(DISTINCT p.name) AS Products
WHERE ProductCount > 1
RETURN s.name AS Supplier,
       ProductCount,
       Products
"""

# 8. Variable-Length Traversal: Multi-tier supplier upstream chain
QUERY_8 = """
MATCH (upstream:Supplier)-[:SUPPLIES_TO*1..3]->(downstream:Supplier {name: 'Supplier A'})
RETURN upstream.name AS TierNSupplier,
       upstream.tier AS TierLevel,
       downstream.name AS DestinationSupplier
"""

# 9. Variable Path: Upstream Tier-2 Supplier through to Plant
QUERY_9 = """
MATCH path = (s:Supplier {tier: 2})-[:SUPPLIES_TO*0..2]->(:Supplier)-[:SUPPLIES]->(:Component)-[:USED_IN]->(:Product)-[:MANUFACTURED_AT]->(pl:Plant)
RETURN path
LIMIT 5
"""

# 10. Shortest Path: Dependency distance between Supplier and Plant
QUERY_10 = """
MATCH (s:Supplier {name: 'Supplier C'}), (pl:Plant {name: 'Hyderabad Plant'})
MATCH p = shortestPath((s)-[*]-(pl))
RETURN length(p) AS HopCount,
       [node in nodes(p) | coalesce(node.name, node.title)] AS PathNodes
"""

# 11. Cross-Border Vulnerability Analysis: Country -> Plant dependency
QUERY_11 = """
MATCH (country:Country {name: 'India'})<-[:LOCATED_IN]-(s:Supplier)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant)
RETURN country.name AS SupplierCountry,
       s.name AS Supplier,
       c.name AS Component,
       p.name AS Product,
       pl.name AS PlantLocation
"""


# --------------------------------------------------
# Main Execution
# --------------------------------------------------
def main():
    try:
        print("Clearing database...")
        run_query(CLEAR_DATABASE)

        print("Populating nodes...")
        run_query(CREATE_NODES)

        print("Populating relationships...")
        run_query(CREATE_RELATIONSHIPS)
        print("Graph database prepared successfully.\n")

        queries = [
            ("1. Direct Component Supply (Single-Hop)", QUERY_1),
            ("2. Full Supply Chain Traversal (Supplier -> Plant)", QUERY_2),
            ("3. Property Filtering (Tier-1 in USA/China)", QUERY_3),
            ("4. Upstream Dependency Analysis (Plant -> Supplier)", QUERY_4),
            ("5. Shipment Destination & Component Traversal", QUERY_5),
            ("6. Aggregation (Component Count per Product)", QUERY_6),
            ("7. Multi-Product Supplier Aggregation", QUERY_7),
            ("8. Variable-Length Traversal (Supplier Tiers)", QUERY_8),
            ("9. Arbitrary Variable-Length Path (Tier 2 to Plant)", QUERY_9),
            ("10. Shortest Path (Supplier C to Hyderabad Plant)", QUERY_10),
            ("11. Cross-Border Country Risk Analysis", QUERY_11),
        ]

        for title, query in queries:
            print(f"=== {title} ===")
            results = run_query(query)
            if not results:
                print("No records found.")
            for row in results:
                print(row)
            print()

    finally:
        driver.close()
        print("Neo4j driver connection closed.")


if __name__ == "__main__":
    main()