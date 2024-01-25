#!/usr/bin/env python3
"""Define a function that List all documents"""

def list_all(mongo_collection):
	"""List all documents"""
	return [item for item in mongo_collection.find()]
