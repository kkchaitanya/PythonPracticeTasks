from src.db import Neo4jConnection
import pandas as pd
db = Neo4jConnection()
print("Connected to Neo4j")

def create_skill(tx, skill):
    query = """
    CREATE (s:Skill {
        skill_id: $Id,
        name: $name,
    })
    """
    tx.run(query, parameters=skill)
def create_candidates(tx,candi):
     query = """
        CREATE (s:Candidate {
            candidate_id: $Id,
            name: $name,
        })
        """
     tx.run(query, parameters=skill)
# Load the CSV file into a DataFrame
df = pd.read_csv('skills.csv')
candidates_df= pd.read_csv('candidates.csv')
# View the first 5 rows
print(df.head())

with db.driver.session() as session:
    for skill in df:
        session.execute_write(
            create_skill,
            skill
        )
    for candi_df in candidates_df:
            session.execute_write(
                create_candidates,
                candi_df
            )
query = """
MATCH (c:Candidate {id: $candidate_id})
MATCH (s:Skill {name: $skill})
MERGE (c)-[:HAS_SKILL]->(s)
"""
session.run(
    query,
    candidate_id="C001",
    skill=".NET"
)      
    

## Get Courses for Alice ##
query = """
MATCH (c:Candidate {name:'Krishna'})-[:HAS_SKILL]->(s:Skill)
RETURN s.name AS skill,c.name as candidate_name
"""

with db.driver.session() as session:
    result = session.run(query)
    for row in result:
        print(row)

#         query = """create(c:course{course_id:$course_id,name:$name}) RETURN c"""
# for course in courses:
#     run_query(query, parameters=course)
# db.close()

## Display Complete Graph
query = """
MATCH (n)-[r]->(m)
RETURN n,r,m
"""

with db.driver.session() as session:
    result = session.run(query)
    for row in result:
        print(row)


#########################
########################
jobs_df= pd.read_csv('jobs.csv')

def create_Job(tx, job):
    query = """
    CREATE (s:Jobs {
        Job_Id: $Id,
        name: $name,
    })
    """
    tx.run(query, parameters=job)
with db.driver.session() as session:
    for job in jobs_df:
        session.execute_write(
            create_Job,
            job
        )
query = """
MATCH (c:Jobs {Job_Id: $Id})
MATCH (s:Skill {name: $skill})
MERGE (c)-[:REQUIRES]->(s)
"""
session.run(
    query,
    Id="J001",
    skill=".NET"
)      

query = """
MATCH (c:Jobs {Job_Id:'J001'})-[:REQUIRES]->(s:Skill)
RETURN s.name AS skill,c.name as Job_name
"""
with db.driver.session() as session:
    result = session.run(query)
    for row in result:
        print(row)
####################
#####################
companies_df= pd.read_csv('companies.csv')

def create_companies_df(tx, companies):
    query = """
    CREATE (s:Companies {
        companie_Id: $Id,
        name: $name,
    })
    """
    tx.run(query, parameters=companies)
with db.driver.session() as session:
    for cmp in companies_df:
        session.execute_write(
            create_companies_df,
            cmp
        )
query = """
MATCH (c:Jobs {Job_Id: $Id})
MATCH (s:Companies {name: $name})
MERGE (c)-[:POSTED_BY]->(s)
"""
session.run(
    query,
    Id="J001",
    name="Microsoft"
)     

query = """
MATCH (c:Jobs {Job_Id:'J001'})-[:REQUIRES]->(s:Companies)
RETURN s.name AS Companie,c.name as Job_name
"""
with db.driver.session() as session:
    result = session.run(query)
    for row in result:
        print(row)

##################
##################
locations_df= pd.read_csv('locations.csv')

def create_locations_df(tx, location):
    query = """
    CREATE (s:Locations {
        Location_Id: $Id,
        name: $name,
    })
    """
    tx.run(query, parameters=location)
with db.driver.session() as session:
    for cmp in locations_df:
        session.execute_write(
            create_locations_df,
            cmp
        )

query = """
MATCH (c:Locations {Location_Id: $Id})
MATCH (s:Companies {name: $name})
MERGE (c)-[:POSTED_BY]->(s)
"""
session.run(
    query,
    Id="LOC001",
    name="Microsoft"
)     
