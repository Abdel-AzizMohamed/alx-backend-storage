#!/usr/bin/env python3
"""Define a function that insert a document"""

def insert_school(mongo_collection, **kwargs):
	"""insert a document"""
	return mongo_collection.insert_one(kwargs).inserted_id
