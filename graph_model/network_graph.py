import numpy as np

class Network:
	def __init__(self):
		"""
		Initiate class attributes
		:attr .network: holds a dictionary of node connections
		:attr ._pairs: currently this class ingests a list of list pairs
			[[0,1], [0,2], ..., [x,y]]
		:attr .complete_nodes: list to hold list of nodes that form complete network
			Currently, the only purpose of this class is to:
				1. generate node mapping
				2. mine the network graph for all complete subnetworks of any size
					My networks are bidirectional and assume no weights
		"""
		self.network = {}
		self._pairs = None
		self.complete_subnet = []

	def buildNetwork(self, data):
		"""
		Currently this method takes in list of lists (sublists could be of > 1d)
		:param data: list of list holding pair data (could be more)
		"""

		# store list of list as ._pairs so we can reference in completenessSearch()
		self._pairs = data

		# store list of unique nodes
		nodes = list(set(item for pair in data for item in pair))

		# iterate through coordinate data and store node connections in list
		# associated with each dictionary node key
		for n in nodes:
			con = []
			for d in data:
				if n in d:
					for i in d:
						if i != n:
							con.append(i)
							break
			# sort the list and store
			self.network[n] = list(sorted(con))

	def completenessSearch(self):
		"""
		The method recursively searches for all
		complete networks present in self.network
		"""
		def treeSearch(network, shared_match, memory):
			if shared_match == []:
				return memory
			else:
				memory.append(memory[-1] + [shared_match[0]])
				set_list = [set(network[i]) for i in memory[-1]]
				shared_match = list(set.intersection(*set_list))
				return treeSearch(network, shared_match, memory)

		for p in self._pairs:
			start_match, start_mem = [p[0]], [[p[1]]]
			self.complete_subnet += treeSearch(self.network, start_match, start_mem)
		# remove duplicates
		self.complete_subnet = [list(g) for g in set(tuple(g) for g in self.complete_subnet)]