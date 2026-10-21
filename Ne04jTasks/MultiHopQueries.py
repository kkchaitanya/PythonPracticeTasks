from neo4j import GraphDatabase
NEO4J_URI="neo4j+s://93dd8a27.databases.neo4j.io"
NEO4J_USERNAME="93dd8a27"
NEO4J_PASSWORD="wZ6NKZmk6a5DZz23oavRAoelrjNJ2LfTy1mAYfEH6tI"
class GraphTraversalDemo:

    def __init__(self):
        self.driver = GraphDatabase.driver(
            NEO4J_URI,
            auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
        )

    def run(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            for row in result:
                print(row)

demo = GraphTraversalDemo()

queries = [
"""
MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)
RETURN s.name,c.name
""",
"""
MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)-[:TEACHES]->(sk:Skill)
RETURN s.name,c.name,sk.name
""",
"""
MATCH (m:Mentor)-[:MENTORS]->(s:Student)
RETURN m.name,s.name
""",
"""
MATCH (s:Student)-[*1..4]-(n)
RETURN s.name,n
LIMIT 10
"""
]

for q in queries:
    print("\nExecuting Query:")
    demo.run(q)

demo.driver.close()