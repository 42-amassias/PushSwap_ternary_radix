#!/usr/bin/python3

import sys
from push_swap import PushSwap

USE_ARGV = False
DEFAULT_VALUES = [ 1, 2, 3 ]

def	argv_to_values(argv: list[str]) -> list[int]:
	return (list(map(int, sum(map(str.split, argv[1:]), []))))

def	check_values(values : list[int]) -> bool:
	l = len(values)
	if l < 1:
		print("There should be at least one value", file=sys.stderr)
		return (False)
	if l != len(set(values)):
		print("There are duplicate values in your input", file=sys.stderr)
		return (False)
	return (True)

if __name__ == "__main__":
	values = argv_to_values(sys.argv) if USE_ARGV else DEFAULT_VALUES
	if not check_values(values):
		exit(1)
	ps = PushSwap[int](values)
