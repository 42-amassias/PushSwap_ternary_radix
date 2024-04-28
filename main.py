#!/usr/bin/python3

import sys
import math

import ternary

from typing import List

from utils import eprint

from push_swap import PushSwap
from ternary import Ternary

from binary_radix import binary_radix

USE_ARGV: bool = False
DEFAULT_VALUES: List[Ternary] = list(map(Ternary, [ 8, 4, 3, 6, 1, 2, 0, 7, 5 ]))

def	argv_to_values(argv: List[str]) -> List[Ternary]:
	return (list(map(Ternary, sum(map(str.split, argv[1:]), []))))

def	check_values(values : List[Ternary]) -> bool:
	if not values:
		eprint("There should be at least one value")
		return (False)
	if len(values) != len(set(values)):
		eprint("There are duplicate values in your input")
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
	eprint(ctx, end='\n\n')
	ternary.radix(ctx)
	eprint('\n', ctx, sep='', end='\n\n')
	ternary.check_result(ctx)
