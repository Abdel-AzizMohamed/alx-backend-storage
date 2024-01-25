"""Define a function that list docments based on topic"""

def schools_by_topic(mongo_collection, topic):
	"""list docments based on topic"""
	filter = {'topics': {'$elemMatch': {'$eq': topic}}}
	return [item for item in mongo_collection.find(filter)]
