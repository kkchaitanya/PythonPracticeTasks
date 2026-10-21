# # Graph Model
# # Nodes
# # Supplier

# # Supplier
# # ---------
# # supplierId
# # name
# # tier

# # Component
# # ----------
# # componentId
# # name

# # Product
# # --------
# # productId
# # name

# # Shipment
# # ---------
# # shipmentId
# # date


# # Country
# # ---------
# # name

# # (Supplier)-[:SUPPLIES]->(Component)

# # (Component)-[:USED_IN]->(Product)

# # (Product)-[:MANUFACTURED_AT]->(Plant)

# # (Supplier)-[:LOCATED_IN]->(Country)

# # (Shipment)-[:CONTAINS]->(Component)

# # (Shipment)-[:DESTINED_FOR]->(Plant)

# # (Supplier)-[:SUPPLIES_TO]->(Supplier)

# # MetalWorks
# #     |
# # SUPPLIES_TO
# #     |
# # ChipMakers
# #     |
# # SUPPLIES
# #     |
# # Processor


# # Data Creation Script (Cypher)

# creat_script= """
# // Countries
# CREATE
# (c1:Country {name:'USA'}),
# (c2:Country {name:'China'}),
# (c3:Country {name:'India'}),
# (c4:Country {name:'Germany'});

# // Suppliers
# CREATE
# (s1:Supplier {supplierId:'S1', name:'Supplier A', tier:1}),
# (s2:Supplier {supplierId:'S2', name:'Supplier B', tier:1}),
# (s3:Supplier {supplierId:'S3', name:'Supplier C', tier:2}),
# (s4:Supplier {supplierId:'S4', name:'Supplier D', tier:2});

# // Components
# CREATE
# (cmp1:Component {componentId:'C1', name:'Processor'}),
# (cmp2:Component {componentId:'C2', name:'Battery'}),
# (cmp3:Component {componentId:'C3', name:'Display'}),
# (cmp4:Component {componentId:'C4', name:'Lithium Cell'});

# // Products
# CREATE
# (p1:Product {productId:'P1', name:'Smartphone'}),
# (p2:Product {productId:'P2', name:'Tablet'}),
# (p3:Product {productId:'P3', name:'Laptop'});

# // Plants
# CREATE
# (pl1:Plant {plantId:'PL1', name:'Hyderabad Plant'}),
# (pl2:Plant {plantId:'PL2', name:'Singapore Plant'}),
# (pl3:Plant {plantId:'PL3', name:'Berlin Plant'});

# // Shipments
# CREATE
# (sh1:Shipment {shipmentId:'SH1'}),
# (sh2:Shipment {shipmentId:'SH2'});
# """

# # Create Relationships

# creat_relationships= """
# MATCH
# (s1:Supplier {name:'Supplier A'}),
# (s2:Supplier {name:'Supplier B'}),
# (s3:Supplier {name:'Supplier C'}),
# (s4:Supplier {name:'Supplier D'}),

# (cmp1:Component {name:'Processor'}),
# (cmp2:Component {name:'Battery'}),
# (cmp3:Component {name:'Display'}),
# (cmp4:Component {name:'Lithium Cell'}),

# (p1:Product {name:'Smartphone'}),
# (p2:Product {name:'Tablet'}),
# (p3:Product {name:'Laptop'}),

# (pl1:Plant {name:'Hyderabad Plant'}),
# (pl2:Plant {name:'Singapore Plant'}),
# (pl3:Plant {name:'Berlin Plant'}),

# (cUSA:Country {name:'USA'}),
# (cChina:Country {name:'China'}),
# (cIndia:Country {name:'India'}),
# (cGer:Country {name:'Germany'}),

# (sh1:Shipment {shipmentId:'SH1'}),
# (sh2:Shipment {shipmentId:'SH2'})

# CREATE

# // Supplier locations
# (s1)-[:LOCATED_IN]->(cUSA),
# (s2)-[:LOCATED_IN]->(cChina),
# (s3)-[:LOCATED_IN]->(cIndia),
# (s4)-[:LOCATED_IN]->(cGermany),

# // Tier 2 dependencies
# (s3)-[:SUPPLIES_TO]->(s1),
# (s4)-[:SUPPLIES_TO]->(s2),

# // Components supplied
# (s1)-[:SUPPLIES]->(cmp1),
# (s1)-[:SUPPLIES]->(cmp2),
# (s2)-[:SUPPLIES]->(cmp3),
# (s3)-[:SUPPLIES]->(cmp4),

# // Components used in products
# (cmp1)-[:USED_IN]->(p1),
# (cmp1)-[:USED_IN]->(p2),
# (cmp2)-[:USED_IN]->(p1),
# (cmp3)-[:USED_IN]->(p2),
# (cmp3)-[:USED_IN]->(p3),
# (cmp4)-[:USED_IN]->(p1),

# // Manufacturing plants
# (p1)-[:MANUFACTURED_AT]->(pl1),
# (p2)-[:MANUFACTURED_AT]->(pl2),
# (p3)-[:MANUFACTURED_AT]->(pl3),

# // Shipments
# (sh1)-[:CONTAINS]->(cmp1),
# (sh1)-[:DESTINED_FOR]->(pl1),

# (sh2)-[:CONTAINS]->(cmp3),
# (sh2)-[:DESTINED_FOR]->(pl3);
# """

# # Required Queries

# # Which Products Depend on Supplier A?

# sq1= """
# MATCH
# (s:Supplier {name:'Supplier A'})
#       -[:SUPPLIES]->
# (c:Component)
#       -[:USED_IN]->
# (p:Product)

# RETURN s.name, c.name, p.name;

# """

# # Which Plants Are Affected if Component X Becomes Unavailable?
# sq2 = """
# MATCH
# (c:Component {name:'Processor'})
#      -[:USED_IN]->
# (p:Product)
#      -[:MANUFACTURED_AT]->
# (pl:Plant)

# RETURN DISTINCT
# c.name,
# p.name,
# pl.name;

# """


# # Find All Suppliers Connected to Product Tablet

# sq3= """

# MATCH
# (s:Supplier)-[:SUPPLIES]->(c:Component)
#              -[:USED_IN]->
# (p:Product {name:'Tablet'})
# RETURN DISTINCT
# s.name,
# c.name;
# """

# # Dependency Path Between Tier-2 Supplier and Plant

# sq4="""
# MATCH path =
# (s:Supplier {name:'Supplier C'})
# -[:SUPPLIES_TO|SUPPLIES*]->
# (c:Component)
# -[:USED_IN]->
# (p:Product)
# -[:MANUFACTURED_AT]->
# (pl:Plant)

# RETURN path;
# """

# #  Components Supplied by Suppliers From a Particular Country

# sq5="""
# MATCH
# (country:Country {name:'China'})
# <-[ :LOCATED_IN ]-
# (s:Supplier)
# -[:SUPPLIES]->
# (c:Component)
# -[:USED_IN]->
# (p:Product)

# RETURN
# country.name,
# s.name,
# c.name,
# p.name;
# """

from neo4j import GraphDatabase
# Neo4j Connection
NEO4J_URI="neo4j+s://93dd8a27.databases.neo4j.io"
NEO4J_USERNAME="93dd8a27"
NEO4J_PASSWORD="wZ6NKZmk6a5DZz23oavRAoelrjNJ2LfTy1mAYfEH6tI"

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)


def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return [record.data() for record in result]


# ----------------------------------
# Create Graph
# ----------------------------------

create_graph = """
MATCH (n) DETACH DELETE n;

// Countries
CREATE
(c1:Country {name:'USA'}),
(c2:Country {name:'China'}),
(c3:Country {name:'India'}),
(c4:Country {name:'Germany'});

// Suppliers
CREATE
(s1:Supplier {supplierId:'S1', name:'Supplier A', tier:1}),
(s2:Supplier {supplierId:'S2', name:'Supplier B', tier:1}),
(s3:Supplier {supplierId:'S3', name:'Supplier C', tier:2}),
(s4:Supplier {supplierId:'S4', name:'Supplier D', tier:2});

// Components
CREATE
(cm1:Component {componentId:'C1', name:'Processor'}),
(cm2:Component {componentId:'C2', name:'Battery'}),
(cm3:Component {componentId:'C3', name:'Display'}),
(cm4:Component {componentId:'C4', name:'Lithium Cell'});

// Products
CREATE
(p1:Product {productId:'P1', name:'Smartphone'}),
(p2:Product {productId:'P2', name:'Tablet'}),
(p3:Product {productId:'P3', name:'Laptop'});

// Plants
CREATE
(pl1:Plant {plantId:'PL1', name:'Hyderabad Plant'}),
(pl2:Plant {plantId:'PL2', name:'Singapore Plant'}),
(pl3:Plant {plantId:'PL3', name:'Berlin Plant'});

// Shipments
CREATE
(sh1:Shipment {shipmentId:'SH1'}),
(sh2:Shipment {shipmentId:'SH2'});
"""

run_query(create_graph)

# ----------------------------------
# Create Relationships
# ----------------------------------

relationships = """
MATCH
(s1:Supplier {name:'Supplier A'}),
(s2:Supplier {name:'Supplier B'}),
(s3:Supplier {name:'Supplier C'}),
(s4:Supplier {name:'Supplier D'}),

(cm1:Component {name:'Processor'}),
(cm2:Component {name:'Battery'}),
(cm3:Component {name:'Display'}),
(cm4:Component {name:'Lithium Cell'}),

(p1:Product {name:'Smartphone'}),
(p2:Product {name:'Tablet'}),
(p3:Product {name:'Laptop'}),

(pl1:Plant {name:'Hyderabad Plant'}),
(pl2:Plant {name:'Singapore Plant'}),
(pl3:Plant {name:'Berlin Plant'}),

(c1:Country {name:'USA'}),
(c2:Country {name:'China'}),
(c3:Country {name:'India'}),
(c4:Country {name:'Germany'}),

(sh1:Shipment {shipmentId:'SH1'}),
(sh2:Shipment {shipmentId:'SH2'})

CREATE

(s1)-[:LOCATED_IN]->(c1),
(s2)-[:LOCATED_IN]->(c2),
(s3)-[:LOCATED_IN]->(c3),
(s4)-[:LOCATED_IN]->(c4),

(s3)-[:SUPPLIES_TO]->(s1),
(s4)-[:SUPPLIES_TO]->(s2),

(s1)-[:SUPPLIES]->(cm1),
(s1)-[:SUPPLIES]->(cm2),
(s2)-[:SUPPLIES]->(cm3),
(s3)-[:SUPPLIES]->(cm4),

(cm1)-[:USED_IN]->(p1),
(cm1)-[:USED_IN]->(p2),
(cm2)-[:USED_IN]->(p1),
(cm3)-[:USED_IN]->(p2),
(cm3)-[:USED_IN]->(p3),
(cm4)-[:USED_IN]->(p1),

(p1)-[:MANUFACTURED_AT]->(pl1),
(p2)-[:MANUFACTURED_AT]->(pl2),
(p3)-[:MANUFACTURED_AT]->(pl3),

(sh1)-[:CONTAINS]->(cm1),
(sh1)-[:DESTINED_FOR]->(pl1),

(sh2)-[:CONTAINS]->(cm3),
(sh2)-[:DESTINED_FOR]->(pl3);
"""

run_query(relationships)

print("\nGraph Created Successfully\n")

# ==================================================
# QUERY 1
# Which products depend on Supplier A?
# ==================================================

query1 = """
MATCH
(s:Supplier {name:'Supplier A'})
-[:SUPPLIES]->
(c:Component)
-[:USED_IN]->
(p:Product)

RETURN s.name AS Supplier,
       c.name AS Component,
       p.name AS Product
"""

print("QUERY 1")
for row in run_query(query1):
    print(row)

# ==================================================
# QUERY 2
# Plants affected if Processor unavailable
# ==================================================

query2 = """
MATCH
(c:Component {name:'Processor'})
-[:USED_IN]->
(p:Product)
-[:MANUFACTURED_AT]->
(pl:Plant)

RETURN c.name AS Component,
       p.name AS Product,
       pl.name AS Plant
"""

print("\nQUERY 2")
for row in run_query(query2):
    print(row)

# ==================================================
# QUERY 3
# Suppliers connected to Tablet
# ==================================================

query3 = """
MATCH
(s:Supplier)
-[:SUPPLIES]->
(c:Component)
-[:USED_IN]->
(p:Product {name:'Tablet'})

RETURN DISTINCT
s.name AS Supplier,
c.name AS Component
"""

print("\nQUERY 3")
for row in run_query(query3):
    print(row)

# ==================================================
# QUERY 4
# Tier-2 supplier dependency path
# ==================================================

query4 = """
MATCH
(s:Supplier {name:'Supplier C'})
-[:SUPPLIES_TO]->
(s1:Supplier)
-[:SUPPLIES]->
(c:Component)
-[:USED_IN]->
(p:Product)
-[:MANUFACTURED_AT]->
(pl:Plant)

RETURN
s.name AS Tier2Supplier,
s1.name AS Tier1Supplier,
c.name AS Component,
p.name AS Product,
pl.name AS Plant
"""

print("\nQUERY 4")
for row in run_query(query4):
    print(row)

# ==================================================
# QUERY 5
# Components supplied from China
# ==================================================

query5 = """
MATCH
(country:Country {name:'China'})
<-[ :LOCATED_IN ]-
(s:Supplier)
-[:SUPPLIES]->
(c:Component)
-[:USED_IN]->
(p:Product)

RETURN
country.name AS Country,
s.name AS Supplier,
c.name AS Component,
p.name AS Product
"""

print("\nQUERY 5")
for row in run_query(query5):
    print(row)

driver.close()

print("\nCompleted Successfully")
