import argparse
import os
from datetime import datetime
from importlib import import_module
from aoc_util.advent import Input

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions.")
    now = datetime.now()
    parser.add_argument("--year", "-y", type=int, help="The year to run.", default=now.year)
    parser.add_argument("--day", "-d", type=int, help="The day to run.", default=now.day)
    parser.add_argument("--path", "-p", type=str, help="Choose a different solution to run.", default="")
    args = parser.parse_args()

    module = import_module(f"src.y{args.year}.d{args.day}")

    if hasattr(module, "main"): 
        getattr(module, "main")(Input(day=args.day, year=args.year, input_path=args.path))
