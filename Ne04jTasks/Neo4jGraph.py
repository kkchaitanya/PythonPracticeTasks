import os
from neo4j import GraphDatabase

# Configuration & Credentials
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
# Reset Graph (Optional, ensures fresh state)
# --------------------------------------------------
CLEAR_GRAPH = """
MATCH (n) DETACH DELETE n
"""

# --------------------------------------------------
# 1. Create Nodes (Chained in a single CREATE statement)
# --------------------------------------------------
CREATE_NODES = """
CREATE
  // Students
  (s1:Student {id: 1, name: 'Alice'}),
  (s2:Student {id: 2, name: 'Bob'}),
  (s3:Student {id: 3, name: 'Charlie'}),
  (s4:Student {id: 4, name: 'David'}),
  (s5:Student {id: 5, name: 'Emma'}),

  // Mentors
  (m1:Mentor {id: 101, name: 'John'}),
  (m2:Mentor {id: 102, name: 'Sarah'}),
  (m3:Mentor {id: 103, name: 'Michael'}),

  // Courses
  (c1:Course {id: 201, title: 'Python Fundamentals'}),
  (c2:Course {id: 202, title: 'Data Science'}),
  (c3:Course {id: 203, title: 'Web Development'}),
  (c4:Course {id: 204, title: 'Cloud Computing'}),

  // Skills
  (sk1:Skill {name: 'Python'}),
  (sk2:Skill {name: 'SQL'}),
  (sk3:Skill {name: 'Machine Learning'}),
  (sk4:Skill {name: 'Angular'}),
  (sk5:Skill {name: 'Azure'}),

  // Projects
  (p1:Project {name: 'Student Portal'}),
  (p2:Project {name: 'Movie Recommendation'}),
  (p3:Project {name: 'E-Commerce Site'}),
  (p4:Project {name: 'Cloud Migration'}),

  // Companies
  (co1:Company {name: 'Microsoft'}),
  (co2:Company {name: 'Google'}),
  (co3:Company {name: 'Amazon'}),
  (co4:Company {name: 'Infosys'})
"""

# --------------------------------------------------
# 2. Create Relationships (Chained MATCH + single CREATE)
# --------------------------------------------------
CREATE_RELATIONSHIPS = """
MATCH
  (sAlice:Student {name: 'Alice'}),
  (sBob:Student {name: 'Bob'}),
  (sCharlie:Student {name: 'Charlie'}),
  (sDavid:Student {name: 'David'}),
  (sEmma:Student {name: 'Emma'}),

  (mJohn:Mentor {name: 'John'}),
  (mSarah:Mentor {name: 'Sarah'}),
  (mMichael:Mentor {name: 'Michael'}),

  (cPy:Course {title: 'Python Fundamentals'}),
  (cDS:Course {title: 'Data Science'}),
  (cWeb:Course {title: 'Web Development'}),
  (cCloud:Course {title: 'Cloud Computing'}),

  (skPy:Skill {name: 'Python'}),
  (skSQL:Skill {name: 'SQL'}),
  (skML:Skill {name: 'Machine Learning'}),
  (skAng:Skill {name: 'Angular'}),
  (skAz:Skill {name: 'Azure'}),

  (pPortal:Project {name: 'Student Portal'}),
  (pMovie:Project {name: 'Movie Recommendation'}),
  (pEcom:Project {name: 'E-Commerce Site'}),
  (pCloud:Project {name: 'Cloud Migration'}),

  (coMS:Company {name: 'Microsoft'}),
  (coGgl:Company {name: 'Google'}),
  (coAmz:Company {name: 'Amazon'}),
  (coInf:Company {name: 'Infosys'})

CREATE
  // Student -> Course
  (sAlice)-[:ENROLLED_IN]->(cPy),
  (sAlice)-[:ENROLLED_IN]->(cDS),
  (sBob)-[:ENROLLED_IN]->(cWeb),
  (sCharlie)-[:ENROLLED_IN]->(cDS),
  (sDavid)-[:ENROLLED_IN]->(cCloud),
  (sEmma)-[:ENROLLED_IN]->(cPy),

  // Mentor -> Course
  (mJohn)-[:TEACHES]->(cPy),
  (mSarah)-[:TEACHES]->(cDS),
  (mMichael)-[:TEACHES]->(cWeb),
  (mJohn)-[:TEACHES]->(cCloud),

  // Course -> Skill
  (cPy)-[:TEACHES_SKILL]->(skPy),
  (cPy)-[:TEACHES_SKILL]->(skSQL),
  (cDS)-[:TEACHES_SKILL]->(skML),
  (cWeb)-[:TEACHES_SKILL]->(skAng),
  (cCloud)-[:TEACHES_SKILL]->(skAz),

  // Student -> Project
  (sAlice)-[:BUILT]->(pPortal),
  (sBob)-[:BUILT]->(pEcom),
  (sCharlie)-[:BUILT]->(pMovie),
  (sDavid)-[:BUILT]->(pCloud),

  // Project -> Skill
  (pPortal)-[:USES]->(skAng),
  (pPortal)-[:USES]->(skSQL),
  (pMovie)-[:USES]->(skML),
  (pEcom)-[:USES]->(skAng),
  (pCloud)-[:USES]->(skAz),

  // Student -> Company
  (sAlice)-[:INTERESTED_IN]->(coMS),
  (sBob)-[:INTERESTED_IN]->(coGgl),
  (sCharlie)-[:INTERESTED_IN]->(coAmz),
  (sDavid)-[:INTERESTED_IN]->(coInf),
  (sEmma)-[:INTERESTED_IN]->(coMS)
"""

# --------------------------------------------------
# Read Queries
# --------------------------------------------------
GET_QUERY1 = """
MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)
RETURN s.name AS Student, c.title AS Course
"""

GET_QUERY2 = """
MATCH (m:Mentor)-[:TEACHES]->(c:Course)
RETURN m.name AS Mentor, c.title AS Course
"""

GET_QUERY3 = """
MATCH (c:Course)-[:TEACHES_SKILL]->(s:Skill)
RETURN c.title AS Course, s.name AS Skill
"""

GET_QUERY4 = """
MATCH (st:Student)-[:BUILT]->(p:Project)
RETURN st.name AS Student, p.name AS Project
"""

GET_QUERY5 = """
MATCH (s:Student)-[:INTERESTED_IN]->(c:Company {name: 'Microsoft'})
RETURN s.name AS Student
"""

GET_QUERY6 = """
MATCH (s:Student {name: 'Alice'})-[:BUILT]->(p:Project)-[:USES]->(sk:Skill)
RETURN DISTINCT sk.name AS Skill
"""

# --------------------------------------------------
# Advanced Queries
# --------------------------------------------------
ADV_Q1 = """
MATCH (st:Student)-[:ENROLLED_IN]->(:Course)-[:TEACHES_SKILL]->(sk:Skill {name: 'Machine Learning'})
RETURN DISTINCT st.name AS Student
"""

ADV_Q2 = """
MATCH (s:Student)-[:INTERESTED_IN]->(:Company {name: 'Microsoft'}),
      (s)-[:ENROLLED_IN]->(:Course)-[:TEACHES_SKILL]->(:Skill {name: 'Python'})
RETURN DISTINCT s.name AS Student
"""

ADV_Q3 = """
MATCH p = (s:Student)-[:BUILT]->(:Project)-[:USES]->(sk:Skill)
RETURN s.name AS Student, sk.name AS Skill
"""

# --------------------------------------------------
# Update & Delete Queries
# --------------------------------------------------
UPDATE_QUERY1 = """
MATCH (s:Student {name: 'Alice'})
SET s.name = 'Alice Johnson'
RETURN s.name AS UpdatedName
"""

UPDATE_QUERY2 = """
MATCH (c:Course {title: 'Data Science'}), (s:Skill {name: 'Python'})
MERGE (c)-[:TEACHES_SKILL]->(s)
RETURN c.title AS Course, s.name AS Skill
"""

UPDATE_QUERY3 = """
MATCH (c:Company {name: 'Infosys'})
SET c.name = 'Infosys Limited'
RETURN c.name AS UpdatedCompany
"""

DELETE_RELATION = """
MATCH (s:Student {name: 'Bob'})-[r:INTERESTED_IN]->(c:Company {name: 'Google'})
DELETE r
"""

DELETE_PROJECT = """
MATCH (p:Project {name: 'Cloud Migration'})
DETACH DELETE p
"""

DELETE_STUDENT = """
MATCH (s:Student {name: 'David'})
DETACH DELETE s
"""


# --------------------------------------------------
# Main Execution
# --------------------------------------------------
def main():
    try:
        print("Resetting database...")
        run_query(CLEAR_GRAPH)

        print("Creating nodes...")
        run_query(CREATE_NODES)

        print("Creating relationships...")
        run_query(CREATE_RELATIONSHIPS)
        print("Graph built successfully!\n")

        print("--- 1. Students & Courses ---")
        for row in run_query(GET_QUERY1):
            print(row)

        print("\n--- 2. Students interested in Microsoft ---")
        for row in run_query(GET_QUERY5):
            print(row)

        print("\n--- 3. Skills used by Alice ---")
        for row in run_query(GET_QUERY6):
            print(row)

        print("\n--- 4. Students interested in Microsoft AND learning Python ---")
        for row in run_query(ADV_Q2):
            print(row)

        # Example update execution
        print("\n--- Running Updates ---")
        res_update = run_query(UPDATE_QUERY1)
        print(f"Updated: {res_update}")

    finally:
        driver.close()
        print("\nDriver connection closed.")


if __name__ == "__main__":
    main()