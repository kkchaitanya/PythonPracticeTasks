from neo4j import GraphDatabase
# https://93dd8a27.databases.neo4j.io/db/93dd8a27/query/v2
NEO4J_URI="neo4j+s://93dd8a27.databases.neo4j.io"
NEO4J_USERNAME="93dd8a27"
NEO4J_PASSWORD="wZ6NKZmk6a5DZz23oavRAoelrjNJ2LfTy1mAYfEH6tI"

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)

# Create Nodes

creat_nodes="""
// Students
CREATE
(s1:Student {id:1, name:'Alice'}),
(s2:Student {id:2, name:'Bob'}),
(s3:Student {id:3, name:'Charlie'}),
(s4:Student {id:4, name:'David'}),
(s5:Student {id:5, name:'Emma'});

// Mentors
CREATE
(m1:Mentor {id:101, name:'John'}),
(m2:Mentor {id:102, name:'Sarah'}),
(m3:Mentor {id:103, name:'Michael'});

// Courses
CREATE
(c1:Course {id:201, title:'Python Fundamentals'}),
(c2:Course {id:202, title:'Data Science'}),
(c3:Course {id:203, title:'Web Development'}),
(c4:Course {id:204, title:'Cloud Computing'});

// Skills
CREATE
(sk1:Skill {name:'Python'}),
(sk2:Skill {name:'SQL'}),
(sk3:Skill {name:'Machine Learning'}),
(sk4:Skill {name:'Angular'}),
(sk5:Skill {name:'Azure'});

// Projects
CREATE
(p1:Project {name:'Student Portal'}),
(p2:Project {name:'Movie Recommendation'}),
(p3:Project {name:'E-Commerce Site'}),
(p4:Project {name:'Cloud Migration'});

// Companies
CREATE
(co1:Company {name:'Microsoft'}),
(co2:Company {name:'Google'}),
(co3:Company {name:'Amazon'}),
(co4:Company {name:'Infosys'});
"""

# Create Relationships
create_relationships= """
// Student -> Course
MATCH (s:Student {name:'Alice'}), (c:Course {title:'Python Fundamentals'})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {name:'Alice'}), (c:Course {title:'Data Science'})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {name:'Bob'}), (c:Course {title:'Web Development'})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {name:'Charlie'}), (c:Course {title:'Data Science'})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {name:'David'}), (c:Course {title:'Cloud Computing'})
CREATE (s)-[:ENROLLED_IN]->(c);

MATCH (s:Student {name:'Emma'}), (c:Course {title:'Python Fundamentals'})
CREATE (s)-[:ENROLLED_IN]->(c);

// Mentor -> Course
MATCH (m:Mentor {name:'John'}), (c:Course {title:'Python Fundamentals'})
CREATE (m)-[:TEACHES]->(c);

MATCH (m:Mentor {name:'Sarah'}), (c:Course {title:'Data Science'})
CREATE (m)-[:TEACHES]->(c);

MATCH (m:Mentor {name:'Michael'}), (c:Course {title:'Web Development'})
CREATE (m)-[:TEACHES]->(c);

MATCH (m:Mentor {name:'John'}), (c:Course {title:'Cloud Computing'})
CREATE (m)-[:TEACHES]->(c);

// Course -> Skill
MATCH (c:Course {title:'Python Fundamentals'}), (s:Skill {name:'Python'})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {title:'Python Fundamentals'}), (s:Skill {name:'SQL'})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {title:'Data Science'}), (s:Skill {name:'Machine Learning'})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {title:'Web Development'}), (s:Skill {name:'Angular'})
CREATE (c)-[:TEACHES_SKILL]->(s);

MATCH (c:Course {title:'Cloud Computing'}), (s:Skill {name:'Azure'})
CREATE (c)-[:TEACHES_SKILL]->(s);

// Student -> Project
MATCH (s:Student {name:'Alice'}), (p:Project {name:'Student Portal'})
CREATE (s)-[:BUILT]->(p);

MATCH (s:Student {name:'Bob'}), (p:Project {name:'E-Commerce Site'})
CREATE (s)-[:BUILT]->(p);

MATCH (s:Student {name:'Charlie'}), (p:Project {name:'Movie Recommendation'})
CREATE (s)-[:BUILT]->(p);

MATCH (s:Student {name:'David'}), (p:Project {name:'Cloud Migration'})
CREATE (s)-[:BUILT]->(p);

// Project -> Skill
MATCH (p:Project {name:'Student Portal'}), (s:Skill {name:'Angular'})
CREATE (p)-[:USES]->(s);

MATCH (p:Project {name:'Student Portal'}), (s:Skill {name:'SQL'})
CREATE (p)-[:USES]->(s);

MATCH (p:Project {name:'Movie Recommendation'}), (s:Skill {name:'Machine Learning'})
CREATE (p)-[:USES]->(s);

MATCH (p:Project {name:'E-Commerce Site'}), (s:Skill {name:'Angular'})
CREATE (p)-[:USES]->(s);

MATCH (p:Project {name:'Cloud Migration'}), (s:Skill {name:'Azure'})
CREATE (p)-[:USES]->(s);

// Student -> Company
MATCH (s:Student {name:'Alice'}), (c:Company {name:'Microsoft'})
CREATE (s)-[:INTERESTED_IN]->(c);

MATCH (s:Student {name:'Bob'}), (c:Company {name:'Google'})
CREATE (s)-[:INTERESTED_IN]->(c);

MATCH (s:Student {name:'Charlie'}), (c:Company {name:'Amazon'})
CREATE (s)-[:INTERESTED_IN]->(c);

MATCH (s:Student {name:'David'}), (c:Company {name:'Infosys'})
CREATE (s)-[:INTERESTED_IN]->(c);

MATCH (s:Student {name:'Emma'}), (c:Company {name:'Microsoft'})
CREATE (s)-[:INTERESTED_IN]->(c);
"""

# Visualize Entire Graph

visualize_graph= """

MATCH (n)
OPTIONAL MATCH (n)-[r]->(m)
RETURN n,r,m;
"""

# READ Queries

# Find all students and courses
get_query1= """
MATCH (s:Student)-[:ENROLLED_IN]->(c:Course)
RETURN s.name AS Student, c.title AS Course;
"""
# Find mentors teaching courses
get_query2 = """
MATCH (m:Mentor)-[:TEACHES]->(c:Course)
RETURN m.name AS Mentor, c.title AS Course;
"""
# Find skills taught in each course
get_query3 ="""
MATCH (c:Course)-[:TEACHES_SKILL]->(s:Skill)
RETURN c.title, s.name;
"""

# Find projects built by students
get_query4="""
MATCH (st:Student)-[:BUILT]->(p:Project)
RETURN st.name, p.name;
"""
# Find students interested in Microsoft

get_query5="""
MATCH (s:Student)-[:INTERESTED_IN]->(c:Company {name:'Microsoft'})
RETURN s;
"""


#Find all skills used by Alice
get_query6="""
MATCH (s:Student {name:'Alice'})-[:BUILT]->(p:Project)-[:USES]->(sk:Skill)
RETURN sk.name;
"""

# UPDATE Queries

# Update Student Name
update_query= """
MATCH (s:Student {name:'Alice'})
SET s.name = 'Alice Johnson'
RETURN s;
"""

#Add New Skill to Existing Course
update_query2="""
MATCH (c:Course {title:'Data Science'})
MATCH (s:Skill {name:'Python'})
MERGE (c)-[:TEACHES_SKILL]->(s);

RETURN c,s;
"""

# Update Company Name
update_query3="""
MATCH (c:Company {name:'Infosys'})
SET c.name='Infosys Limited'
RETURN c;
"""

# DELETE Queries
# Delete a Relationship
delete_relation= """
MATCH (s:Student {name:'Bob'})
-[r:INTERESTED_IN]->
(c:Company {name:'Google'})
DELETE r;
"""


# Delete a Project
delete_project = """
MATCH (p:Project {name:'Cloud Migration'})
DETACH DELETE p;
"""

# Delete a Student

delete_student= """
MATCH (s:Student {name:'David'})
DETACH DELETE s;
"""


# Advanced Queries

# Students learning Machine Learning

get_q1= """
MATCH (st:Student)-[:ENROLLED_IN]->(:Course)
      -[:TEACHES_SKILL]->(sk:Skill {name:'Machine Learning'})
RETURN st.name;
"""

# Students interested in Microsoft and learning Python


get_q2 = """
MATCH (s:Student)-[:INTERESTED_IN]->(:Company {name:'Microsoft'})
MATCH (s)-[:ENROLLED_IN]->(:Course)-[:TEACHES_SKILL]->(:Skill {name:'Python'})
RETURN s.name;
"""

# Path from Student to Skill Through Project

get_q3= """
MATCH p=(s:Student)-[:BUILT]->(:Project)-[:USES]->(sk:Skill)
RETURN p;
"""

