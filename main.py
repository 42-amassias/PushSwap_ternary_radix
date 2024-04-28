#!/usr/bin/python3

import sys

from typing import List

from push_swap import PushSwap
from ternary import Ternary

from binary_radix import binary_radix

USE_ARGV: bool = False
DEFAULT_VALUES: List[Ternary] = list(map(Ternary, [ 8, 4, 3, 6, 1, 2, 0, 7, 5 ]))

def	argv_to_values(argv: List[str]) -> List[Ternary]:
	return (list(map(Ternary, sum(map(str.split, argv[1:]), []))))

def	check_values(values : List[Ternary]) -> bool:
	if not values:
		print("There should be at least one value", file=sys.stderr)
		return (False)
	if len(values) != len(set(values)):
		print("There are duplicate values in your input", file=sys.stderr)
		return (False)
	return (True)

if __name__ == "__main__":
	values: List[Ternary] = DEFAULT_VALUES
	if USE_ARGV:
		values: List[Ternary] = argv_to_values(sys.argv)
	if not check_values(values):
		exit(1)
	if values == sorted(values):
		exit(0)
	ctx: PushSwap[Ternary] = PushSwap[Ternary](values, Ternary)
	binary_radix(ctx)
	print(ctx)
