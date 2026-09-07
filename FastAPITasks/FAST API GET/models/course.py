from typing import List


class Course:
    course_name: str
    mentor: str
    duration: str
    topics: List[str]
    def __init__(self,course_name,mentor,duration,topics):
        self.course_name=course_name
        self.mentor=mentor
        self.duration=duration
        self.topics=topics
