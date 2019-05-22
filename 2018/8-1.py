#! /usr/bin/env python

import os
import sys

#read input
with open('8-input.txt','r') as f:
	#content = """2 3 0 3 10 11 12 2 1 1 1 0 1 5 99 0 1 2 2 1 1 2""".split(' ')#f.read().split(' ')
	content = """2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2""".split(' ')

content = [int(x) for x in content]

#header has two numbers exactly: # nodes, # of metadata entries.
#original idea was to use recursion to calculate this, but max recursion depth hit and python doesn't support TCO

"""[10:39 AM] Ves Zappa: Wait, I've looked more closely at my solution. I think the first part is no longer recursive
[10:43 AM] Ves Zappa: So, what I did was create a Node class that keeps track of the number of children and the number of children we've processed and the value of children. That way we can walk through the data in a linear fashion and we know whether or not we we're processing metadata (the current node has no more unprocessed children) or busy with processing children (there are children)"""

class Tree():

	def __init__(self,key):
		self.processed = False
		self.current_depth = 0
		self.current_index = 2
		self.children_list = [key[0]]
		self.metadata_list = [key[1]]
		
	def walk(self):
		raise NotImplementedError


tree = Tree(content)

while not tree.processed:
	tree.walk()

print(tree.metadata_sum)
