from db import Neo4jConnection
import pandas as pd
db = Neo4jConnection()
df = pd.read_csv('../data/skills.csv')
# View the first 5 rows
print(df.head())
def create_skill(tx, skill):
    # Notice there is absolutely NO comma after $Skill
    query = """
    CREATE (s:Skill { skill_id: $Id, name: $Skill } ) RETURN s
    """
    tx.run(query, parameters=skill)
with db.driver.session() as session:
    for skill_row in df.to_dict('records'):
        session.execute_write(create_skill, skill_row)
candidates_df = pd.read_csv('../data/candidates.csv')
# View the first 5 rows
print(candidates_df.head())
def create_candidate(tx, skill):
    # Notice there is absolutely NO comma after $Skill
    query = """
    CREATE (c:Candidate { candidate_id: $Id, name: $name } ) RETURN c
    """
    tx.run(query, parameters=skill)
with db.driver.session() as session:
    for candi_row in candidates_df.to_dict('records'):
        print(candi_row)
        session.execute_write(create_candidate, candi_row)
query = """
MATCH (c:Candidate {candidate_id: $c_id})
MATCH (s:Skill {name: $s_name})
MERGE (c)-[:HAS_SKILL]->(s)
"""

with db.driver.session() as session:
    session.run(
        query,
        c_id="C002",      # Maps to $c_id -> looks up candidate_id: "C002"
        s_name="Azure"    # Maps to $s_name -> looks up name: "Azure"
    )


with db.driver.session() as session:
    session.run(
        query,
        c_id="C001",      # Maps to $c_id -> looks up candidate_id: "C002"
        s_name="Machine Learning"    # Maps to $s_name -> looks up name: "Azure"
    )
    session.run(
            query,
            c_id="C003",      # Maps to $c_id -> looks up candidate_id: "C002"
            s_name="Machine Learning"    # Maps to $s_name -> looks up name: "Azure"
        )
with db.driver.session() as session:
    session.run(
        query,
        c_id="C001",      # Maps to $c_id -> looks up candidate_id: "C002"
        s_name="C#"    # Maps to $s_name -> looks up name: "Azure"
    )
    session.run(
            query,
            c_id="C001",      # Maps to $c_id -> looks up candidate_id: "C002"
            s_name=".NET"    # Maps to $s_name -> looks up name: "Azure"
        )
    session.run(
            query,
            c_id="C001",      # Maps to $c_id -> looks up candidate_id: "C002"
            s_name="Angular"    # Maps to $s_name -> looks up name: "Azure"
        )
    session.run(
                query,
                c_id="C001",      # Maps to $c_id -> looks up candidate_id: "C002"
                s_name="SQL"    # Maps to $s_name -> looks up name: "Azure"
            )
jobs_df = pd.read_csv('../data/jobs.csv')
# View the first 5 rows
print(jobs_df.head())
def create_job(tx, jb):
    # Notice there is absolutely NO comma after $Skill
    query = """
    CREATE (j:Job { job_id: $Id, name: $name } ) RETURN j
    """
    tx.run(query, parameters=jb)
with db.driver.session() as session:
    for job_row in jobs_df.to_dict('records'):
        print(job_row)
        session.execute_write(create_job, job_row)
# 1. Clean, fixed query string
query = """
MATCH (j:Job {job_id: $j_id})
MATCH (s:Skill {name: $s_name})
MERGE (j)-[:REQUIRES]->(s)
"""

with db.driver.session() as session:
    # 2. Parameters MUST match $j_id and $s_name exactly
    session.run(
        query,
        j_id="J001",      # Changed from c_id to j_id
        s_name="C#"       # Matches $s_name
    )
    session.run(
        query,
        j_id="J001",
        s_name=".NET"
    )
    session.run(
        query,
        j_id="J001",
        s_name="Angular"
    )
with db.driver.session() as session:
     session.run(
            query,
            j_id="J001",
            s_name="SQL"
        )
     session.run(
                 query,
                 j_id="J001",
                 s_name="Azure"
             )
industries_df = pd.read_csv('../data/industries.csv')
# View the first 5 rows
print(industries_df.head())
def create_industries(tx, ind):
    # Notice there is absolutely NO comma after $Skill
    query = """
    CREATE (i:Industrie { industrie_id: $Id, name: $name } ) RETURN i
    """
    tx.run(query, parameters=ind)
with db.driver.session() as session:
    for industries_row in industries_df.to_dict('records'):
        print(industries_row)
        session.execute_write(create_industries, industries_row)
query = """
MATCH (j:Job {job_id: $j_id})
MATCH (s:Industrie {name: $s_name})
MERGE (j)-[:BELONGS_TO]->(s)
"""
with db.driver.session() as session:
    # 2. Parameters MUST match $j_id and $s_name exactly
    session.run(
        query,
        j_id="J001",      # Changed from c_id to j_id
        s_name="Banking"       # Matches $s_name
    )
    session.run(
        query,
        j_id="J001",
        s_name="Insurance"
    )
    session.run(
            query,
            j_id="J001",
            s_name="Healthcare"
        )
    session.run(
                query,
                j_id="J001",
                s_name="Retail"
            )
companies_df = pd.read_csv('../data/companies.csv')
# View the first 5 rows
print(companies_df.head())    
def create_companies(tx, com):
    # Notice there is absolutely NO comma after $Skill
    query = """
    CREATE (c:Companies { companies_id: $Id, name: $name } ) RETURN c
    """
    tx.run(query, parameters=com)
with db.driver.session() as session:
    for companies_row in companies_df.to_dict('records'):
        print(companies_row)
        session.execute_write(create_companies, companies_row)  
query = """
MATCH (j:Job {job_id: $j_id})
MATCH (c:Companies {name: $s_name})
MERGE (j)-[:POSTED_BY]->(c)
"""
with db.driver.session() as session:
    # 2. Parameters MUST match $j_id and $s_name exactly
    session.run(
        query,
        j_id="J001",      # Changed from c_id to j_id
        s_name="Microsoft"       # Matches $s_name
    )
    session.run(
            query,
            j_id="J001",      # Changed from c_id to j_id
            s_name="Capgemini"       # Matches $s_name
        )
    session.run(
                query,
                j_id="J001",      # Changed from c_id to j_id
                s_name="Accenture"       # Matches $s_name
            )
location_df = pd.read_csv('../data/locations.csv')
# View the first 5 rows
print(location_df.head())  
def create_locations(tx, com):
    # Notice there is absolutely NO comma after $Skill
    query = """
    CREATE (c:Locations { location_id: $Id, name: $name } ) RETURN c
    """
    tx.run(query, parameters=com)
with db.driver.session() as session:
    for location_row in location_df.to_dict('records'):
        print(location_row)
        session.execute_write(create_locations, location_row)
query = """
MATCH (l:Locations {name: $loc_name})
MATCH (c:Companies {name: $com_name})
MERGE (c)-[:LOCATED_IN]->(l)
"""

with db.driver.session() as session:
    session.run(
        query,
        loc_name="Hyderabad",      
        com_name="Microsoft"       
    )
    session.run(
        query,
        loc_name="Hyderabad",      
        com_name="Capgemini"       
    )
### Select Operations ####
query = """
MATCH (c:Candidate {name: $c_name})-[:HAS_SKILL]->(s:Skill)<-[:REQUIRES]-(j:Job)
RETURN j.name AS job_title, count(s) AS match_score
ORDER BY match_score DESC
"""

with db.driver.session() as session:
    result = session.run(query, c_name="Rahul")
    for record in result:
        print(f"Job: {record['job_title']} | Skills Matched: {record['match_score']}")
with db.driver.session() as session:
    result = session.run(query, c_name="Krishna")
    for record in result:
        print(f"Job: {record['job_title']} | Skills Matched: {record['match_score']}")

## Location-Based Skill Demand ##
query = """
MATCH (l:Location {name: $location_name})<-[:LOCATED_IN]-(c:Company)
MATCH (c)<-[:POSTED_BY]-(j:Job)-[:REQUIRES]->(s:Skill)
RETURN s.name AS skill_name, count(j) AS job_count
ORDER BY job_count DESC
LIMIT 5
"""

with db.driver.session() as session:
    result = session.run(query, location_name="Hyderabad")
    print("--- In-Demand Skills in Hyderabad ---")
    for record in result:
        print(f"Skill: {record['skill_name']} | Openings: {record['job_count']}")
## Industry Popularity Contest ##
query = """
MATCH (i:Industry)<-[:BELONGS_TO]-(c:Company)<-[:POSTED_BY]-(j:Job)
RETURN i.name AS industry_name, count(j) AS total_jobs
ORDER BY total_jobs DESC
"""

with db.driver.session() as session:
    result = session.run(query)
    print("--- Job Volume by Industry ---")
    for record in result:
        print(f"Industry: {record['industry_name']} | Total Jobs: {record['total_jobs']}")
# Co-occurring Skill Recommendations (Skill-to-Skill)
query = """
MATCH (s1:Skill {name: $target_skill})<-[:REQUIRES]-(j:Job)-[:REQUIRES]->(s2:Skill)
WHERE s1 <> s2
RETURN s2.name AS related_skill, count(j) AS frequency
ORDER BY frequency DESC
LIMIT 3
"""

with db.driver.session() as session:
    result = session.run(query, target_skill="Azure")
    print("--- Skills frequently paired with Azure ---")
    for record in result:
        print(f"Related Skill: {record['related_skill']} (Appears in {record['frequency']} jobs)")
