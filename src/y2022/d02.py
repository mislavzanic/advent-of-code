#!/usr/bin/env python3

def main():
	l = [x.strip() for x in open('input').readlines()]
	score = {'X':0, 'Y':3, 'Z':6, 'A': 1, 'B':2, 'C':3}
	win = {'Y':'A', 'X':'C', 'Z':'B'}
	win2 = {'A':'Z', 'C':'Y', 'B':'X'}
	mapping = {'X': 'A', 'Y':'B', 'Z':'C'}
	s = []
	for item in l:
		x = item.split(' ')
		if x[1] == 'Y':
			s.append(score[x[0]] + score[x[1]])
		if x[1] == 'X':
			s.append(score[mapping[win2[x[0]]]] + score[x[1]])
		if x[1] == 'Z':
			for k in win.keys():
				if win[k] == x[0]:
					s.append(score[mapping[k]] + score[x[1]])
		print(s)

	print(sum(s))

if __name__ == '__main__':
	main()
