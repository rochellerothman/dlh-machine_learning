#!/usr/bin/env python3
"""Module for updating school topics"""


def update_topics(mongo_collection, name, topics):
    """Updates the topics of all school documents with the given name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
