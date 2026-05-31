#!/usr/bin/env python3
"""Module for returning top students by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    students = list(mongo_collection.find())

    for student in students:
        topics = student.get("topics", [])
        avg_score = sum(
            topic.get("score", 0) for topic in topics
        ) / len(topics)

        student["averageScore"] = avg_score

    return sorted(
        students,
        key=lambda student: student["averageScore"],
        reverse=True
    )
