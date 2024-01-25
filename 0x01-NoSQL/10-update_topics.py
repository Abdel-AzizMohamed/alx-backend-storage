#!/usr/bin/env python3
"""Define a function that update documents"""

def update_topics(mongo_collection, name, topics):
	"""update documents"""
	mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
