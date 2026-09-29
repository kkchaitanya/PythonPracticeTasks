from src.db import Neo4jConnection

db = Neo4jConnection()
print("Connected to Neo4j")
db.close()