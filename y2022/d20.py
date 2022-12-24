#!/usr/bin/env python3

from typing import get_origin
# from z3 import If, Bool, Solver, And, Int, Tactic
import itertools as it
import functools
from collections import Counter, defaultdict, deque
from queue import PriorityQueue
import re
import ast
import math
from advent import Input

day = Input(20,2022)
# day = Input(20,2022, 'input/20.ex')

class Node:
	def __init__(self,idx,value):
		self.value = value
		self.idx = idx
		self.next = None
		self.prev = None

	def __str__(self):
		return str(self.value)# + ',' + str(self.idx)

class LinkedList:
	def __init__(self,head=None):
		self.head = head

	def append(self, new_node):
		if self.head is None:
			self.head = new_node
			self.head.next = new_node
			self.head.prev = new_node

		else:
			temp = self.head.prev
			temp.next = new_node
			self.head.prev = new_node
			new_node.prev = temp
			new_node.next = self.head

	def find(self, idx, num):
		i = 0
		curr = self.head
		while curr and (curr.value != num or curr.idx != idx):
			curr = curr.next
			i += 1
		assert curr != None
		assert curr.value == num and curr.idx == idx, (curr.value, curr.idx, num, idx)
		return curr, i

	def rotate(self, node, direction):
		if direction:
			n = node.next
			self.delete(node)
			self.insert(n, node)
		else:
			n = node.prev
			self.delete(node)
			self.insert_prev(n, node)

	def delete(self, node):
		p, n = node.prev, node.next
		n.prev = p
		p.next = n
		if node == self.head:
			self.head = n

		node.prev = None
		node.next = None

	def insert(self, at, node):
		n = at.next
		at.next = node
		node.prev = at
		node.next = n
		n.prev = node

	def insert_prev(self, at, node):
		n = at.prev
		at.prev = node
		node.prev = n
		node.next = at
		n.next = node

	def __str__(self):
		temp = self.head
		s = ''
		while temp:
			s += str(temp)
			s += ' '
			temp = temp.next
			if temp == self.head: break
		return s


ll = list(map(int, day.lines))

zero = None

LL = LinkedList()
for x in enumerate(ll):
	if x[1] == 0: zero = x
	LL.append(Node(x[0], x[1] * 811589153))
	ll[x[0]] = x[1] * 811589153

N = len(ll)
for _ in range(10):
	for x in enumerate(ll):
		i, num = x

		if num == 0:
			zero = x
			continue

		node, _ = LL.find(*x)

		temp = node
		much = num % (N-1) if num >= 0 else -num % (N-1)

		for _ in range(much):
			LL.rotate(node, num >= 0)
			temp = temp.next if num >= 0 else temp.prev


		# print(LL)

	# print(-10 % 7)
zero_node,_ = LL.find(*zero)
curr = zero_node
s = 0
for i in range(3):
	x = 1000
	while x:
		curr = curr.next
		x -= 1
	s += curr.value
	print(curr.value)
print(s)

# print(i,j,k, N, arr)
