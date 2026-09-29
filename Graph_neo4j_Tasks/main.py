from neo4j import GraphDatabase
# https://93dd8a27.databases.neo4j.io/db/93dd8a27/query/v2
NEO4J_URI="neo4j+s://93dd8a27.databases.neo4j.io"
NEO4J_USERNAME="93dd8a27"
NEO4J_PASSWORD="wZ6NKZmk6a5DZz23oavRAoelrjNJ2LfTy1mAYfEH6tI"

driver = GraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USERNAME, NEO4J_PASSWORD)
)

create_query = """
// Students
CREATE
(s1:Student {id:1, name:'Alice'}),
(s2:Student {id:2, name:'Bob'}),
(s3:Student {id:3, name:'Charlie'}),
(s4:Student {id:4, name:'Diana'})

// Mentors
CREATE
(m1:Mentor {id:1, name:'John'}),
(m2:Mentor {id:2, name:'Sarah'}),
(m3:Mentor {id:3, name:'Michael'})

// Courses
CREATE
(c1:Course {id:101, title:'Python Fundamentals'}),
(c2:Course {id:102, title:'Data Science'}),
(c3:Course {id:103, title:'Web Development'}),
(c4:Course {id:104, title:'Machine Learning'})

// Skills
CREATE
(sk1:Skill {name:'Python'}),
(sk2:Skill {name:'SQL'}),
(sk3:Skill {name:'JavaScript'}),
(sk4:Skill {name:'Machine Learning'}),
(sk5:Skill {name:'Data Analysis'})

// Projects
CREATE
(p1:Project {name:'E-Commerce App'}),
(p2:Project {name:'Recommendation System'}),
(p3:Project {name:'Portfolio Website'})

// Companies
CREATE
(co1:Company {name:'Microsoft'}),
(co2:Company {name:'Google'}),
(co3:Company {name:'Amazon'})
"""

relationship_query = """
MATCH
(s1:Student {name:'Alice'}),
(s2:Student {name:'Bob'}),
(s3:Student {name:'Charlie'}),
(s4:Student {name:'Diana'}),
(c1:Course {title:'Python Fundamentals'}),
(c2:Course {title:'Data Science'}),
(c3:Course {title:'Web Development'}),
(c4:Course {title:'Machine Learning'}),
(m1:Mentor {name:'John'}),
(m2:Mentor {name:'Sarah'}),
(m3:Mentor {name:'Michael'}),
(sk1:Skill {name:'Python'}),
(sk2:Skill {name:'SQL'}),
(sk3:Skill {name:'JavaScript'}),
(sk4:Skill {name:'Machine Learning'}),
(sk5:Skill {name:'Data Analysis'}),
(p1:Project {name:'E-Commerce App'}),
(p2:Project {name:'Recommendation System'}),
(p3:Project {name:'Portfolio Website'}),
(co1:Company {name:'Microsoft'}),
(co2:Company {name:'Google'}),
(co3:Company {name:'Amazon'})

CREATE
// Enrollments
(s1)-[:ENROLLED_IN]->(c1),
(s1)-[:ENROLLED_IN]->(c2),
(s2)-[:ENROLLED_IN]->(c1),
(s2)-[:ENROLLED_IN]->(c3),
(s3)-[:ENROLLED_IN]->(c2),
(s3)-[:ENROLLED_IN]->(c4),
(s4)-[:ENROLLED_IN]->(c3),

// Mentor Teaching
(m1)-[:TEACHES]->(c1),
(m1)-[:TEACHES]->(c2),
(m2)-[:TEACHES]->(c3),
(m3)-[:TEACHES]->(c4),

// Course Skills
(c1)-[:TEACHES_SKILL]->(sk1),
(c2)-[:TEACHES_SKILL]->(sk2),
(c2)-[:TEACHES_SKILL]->(sk5),
(c3)-[:TEACHES_SKILL]->(sk3),
(c4)-[:TEACHES_SKILL]->(sk4),

// Projects
(s1)-[:BUILT]->(p1),
(s2)-[:BUILT]->(p3),
(s3)-[:BUILT]->(p2),

// Project Skills
(p1)-[:USES]->(sk1),
(p1)-[:USES]->(sk3),
(p2)-[:USES]->(sk4),
(p3)-[:USES]->(sk3),

// Companies
(s1)-[:INTERESTED_IN]->(co1),
(s2)-[:INTERESTED_IN]->(co2),
(s3)-[:INTERESTED_IN]->(co3)
"""

with driver.session() as session:
    session.run(create_query)
    session.run(relationship_query)

print("Graph created successfully!")

driver.close()