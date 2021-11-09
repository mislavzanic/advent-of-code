import sys

if __name__ == '__main__':
    _, day, infile = sys.argv

    inlist = [x.strip() for x in open(infile)]

    if day == '1':
        ...
    else: raise NotImplementedError()
