import functools
import os
import re
from collections import defaultdict
import itertools as it
import random
import sys
import aoc_util.advent as aoc

day = aoc.Input(19, 2015)

rules, goal = day.string.split('\n\n')
values = []
goal = goal.strip()
splitted = defaultdict(list)
C = []
# grammar = defaultdict(str)
grammar = defaultdict(list)
for rule in rules.split('\n'):
	if rule == '': continue
	a, b = rule.split(' => ')
	# grammar[b] = a
	grammar[a].append(b)
	splitted[b] = re.findall('[A-Z][^A-Z]*', b)
	values.append(b)


for k,v in splitted.items():
	for item in v:
		if item not in grammar.keys():
			C.append(item)


def match_rules(word, start, end, rules) -> int:
	global goal, DP
	rule_list = []
	key = (word, start, end, rules)

	if key in DP:
		return DP[key]

	if word[start:end] == rules:
		return match(word,start,end,rules)

	rule_list = re.findall('[A-Z][^A-Z]*', rules)

	if len(rule_list) == 1:
		return match(word, start, end, rule_list[0])
	if len(rule_list) == 0:
		return -1


	for i in range(start + 1, end):
		if word[i:end][0].islower():
			DP[key] = -1
			continue
		m1 = match(word, start, i, rule_list[0])
		m2 = match_rules(word, i, end, ''.join(rule_list[1:]))
		if m1 != -1 and m2 != -1:
			DP[key] = m1 + m2
			return m1 + m2
	return -1


DP = {}
def match(word, start, end, rule) -> int:
	global grammar, values, DP, C

	key = (word, start, end, rule)

	if word[start:end][0].islower():
		DP[key] = -1
		return -1

	if key in DP: return DP[key]

	if word[start:end] in C:
		DP[key] = -1 if word[start:end] != rule else 0
		return DP[key]

	if word[start:end] == rule:
		DP[key] = 0
		return 0

	else:
		for option in grammar[rule]:
			m = match_rules(word, start, end, option)
			if m != -1:
				DP[key] = m + 1
				return m + 1
	DP[key] = -1
	return -1


# print(goal, grammar)
print(match(goal, 0, len(goal), 'e'), 2)

# print(dfs(goal))
# print(bottomUp('e'))
