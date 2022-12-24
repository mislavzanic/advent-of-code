#!/usr/bin/env python3

import itertools as it
from collections import defaultdict

	def main():
	l = [x.strip() for x in open('input').readlines()]
	def put(s, c):
		for char in c:
			s.add(char)
		return s

	ll = []
	d = {k:v for k,v in zip('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', [i for i in range(1,53)])}
	batch = []
	for item in l:
		batch.append(item)
		if len(batch) == 3:
			s = [set(), set(), set()]
			for i, item in enumerate(batch):
				for char in item:
					s[i].add(char)

			for i in range(3):
				s[i] &= s[(i + 1) % 3]
				s[i] &= s[(i + 2) % 3]

			ll.append(d[s[0].pop()])
			batch = []


	print(sum(ll))


if __name__ == '__main__':
	main()
