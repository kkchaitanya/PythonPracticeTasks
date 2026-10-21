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
    """Execute a single Cypher query and return results as a list of dictionaries."""
    with driver.session() as session:
        result = session.run(query, parameters or {})
        return [record.data() for record in result]


# --------------------------------------------------
# Cypher Statements (Single statements per query)
# --------------------------------------------------

CLEAR_DATABASE = """
MATCH (n) DETACH DELETE n
"""

# Chained into a single CREATE statement using commas
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

QUERY_1 = """
MATCH (s:Supplier {name: 'Supplier A'})-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)
RETURN s.name AS Supplier,
       c.name AS Component,
       p.name AS Product
"""

QUERY_2 = """
MATCH (c:Component {name: 'Processor'})-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant)
RETURN DISTINCT
       c.name AS Component,
       p.name AS Product,
       pl.name AS Plant
"""

QUERY_3 = """
MATCH (s:Supplier)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product {name: 'Tablet'})
RETURN DISTINCT
       s.name AS Supplier,
       c.name AS Component
"""

QUERY_4 = """
MATCH (s:Supplier {name: 'Supplier C'})-[:SUPPLIES_TO]->(s1:Supplier)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)-[:MANUFACTURED_AT]->(pl:Plant)
RETURN s.name AS Tier2Supplier,
       s1.name AS Tier1Supplier,
       c.name AS Component,
       p.name AS Product,
       pl.name AS Plant
"""

QUERY_5 = """
MATCH (country:Country {name: 'China'})<-[:LOCATED_IN]-(s:Supplier)-[:SUPPLIES]->(c:Component)-[:USED_IN]->(p:Product)
RETURN country.name AS Country,
       s.name AS Supplier,
       c.name AS Component,
       p.name AS Product
"""


# --------------------------------------------------
# Main Execution
# --------------------------------------------------

def main():
    try:
        print("Clearing existing data...")
        run_query(CLEAR_DATABASE)

        print("Creating graph nodes...")
        run_query(CREATE_NODES)

        print("Creating graph relationships...")
        run_query(CREATE_RELATIONSHIPS)
        print("Graph populated successfully.\n")

        print("=== QUERY 1: Products depending on Supplier A ===")
        for record in run_query(QUERY_1):
            print(record)

        print("\n=== QUERY 2: Plants affected if Processor is unavailable ===")
        for record in run_query(QUERY_2):
            print(record)

        print("\n=== QUERY 3: Suppliers connected to Tablet ===")
        for record in run_query(QUERY_3):
            print(record)

        print("\n=== QUERY 4: Tier-2 supplier dependency path ===")
        for record in run_query(QUERY_4):
            print(record)

        print("\n=== QUERY 5: Components supplied from China ===")
        for record in run_query(QUERY_5):
            print(record)

    finally:
        driver.close()
        print("\nNeo4j driver connection closed.")


if __name__ == "__main__":
    main()