from collections import Counter

def next(curr):
    return (curr * 252533) % 33554393

def main():
    row, column = 3010, 3019
    # row, column = 6, 10
    c = Counter()

    def run():
        c[(0,0)] = 20151125
        for i in range(1, row * column):
            for j in range(0, i+1):
                c[(i - j,j)] = next(c[(0,i-1)] if j == 0 else c[(i+1-j,j-1)])
                if i - j == row and j == column:
                    return

    run()
    print(c[(row-1, column-1)])

if __name__ == '__main__':
    main()
