import argparse
from datetime import datetime
from importlib import import_module
from aoc_util.advent import Input

def run(module, func, part):
    if not hasattr(module, func): return

    solution = getattr(module, func)(inp)
    if solution is None: return

    print(f'Part {part}: {solution}')
    if args.submit == int(part):
        inp.submit(solution, part=args.submit)

def setup_parser():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    now = datetime.now()
    parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    parser.add_argument("--path", "-p", type=str, help="Choose a different solution to run.", default="")
    parser.add_argument("--submit", "-s", type=int, help="Submit solution.", default=0)
    return parser

if __name__ == '__main__':
    parser = setup_parser()
    args = parser.parse_args()

    module = import_module(f"src.y{args.year}.d{args.day}")
    inp = Input(day=args.day, year=args.year, input_path=args.path)

    for i in "12":
        run(module, "p" + i, i)
