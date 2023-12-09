from aoc_util.advent import Input

def iterate(line, insert_pos, ret_pos, extrapolate):
    seqs = [list(map(int, line.split()))]
    while True:
        next_seq = [seqs[-1][i+1] - seqs[-1][i] for i in range(len(seqs[-1]) - 1)]
        seqs.append(next_seq)
        if not any(next_seq):
            break
    for i in range(len(seqs)-1):
        seqs[-i-2].insert(insert_pos(seqs[-i-2]), extrapolate(seqs[-i-1], seqs[-i-2]))
    return seqs[0][ret_pos]

def p2(day: Input):
    return sum([iterate(line, lambda _: 0, 0, lambda x,y: y[0] - x[0]) for line in day.lines()])

def p1(day: Input):
    return sum([iterate(line, lambda x: len(x), -1, lambda x,y: x[-1] + y[-1]) for line in day.lines()])
