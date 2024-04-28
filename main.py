#!/usr/bin/python3

import sys
import math
import random

import ternary

from typing import List

from utils import eprint

from push_swap import PushSwap
from ternary import Ternary

from binary_radix import binary_radix

# 8 4 3 6 1 2 0 7 5

USE_ARGV: bool = True
USE_RANDOM: bool = True
if USE_RANDOM:
	DEFAULT_VALUES_COUNT = 8
	DEFAULT_VALUES = list(range(DEFAULT_VALUES_COUNT))
	random.shuffle(DEFAULT_VALUES)
else:
	DEFAULT_VALUES = [7, 8, 4, 5, 3, 10, 9, 6, 1, 2]
DEFAULT_VALUES: List[Ternary] = list(map(Ternary, DEFAULT_VALUES))

def	argv_to_values(argv: List[str]) -> List[Ternary]:
	return (list(map(Ternary, map(int, sum(map(str.split, argv[1:]), [])))))

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
