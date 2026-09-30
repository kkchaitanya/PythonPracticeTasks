from neo4j import GraphDatabase
URI = "neo4j+s://93dd8a27.databases.neo4j.io" 
AUTH = ("93dd8a27", "wZ6NKZmk6a5DZz23oavRAoelrjNJ2LfTy1mAYfEH6tI")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()
    driver.session().run("""
        MATCH (n)
        DETACH DELETE n
    """)
    print("Connection successful!")

# db.close()