#!/usr/bin/python3

import sys
import random

import ternary
import binary

from typing import List

from utils import eprint

from push_swap import PushSwap

from number import Binary
from number import Ternary

USE_BINARY: bool = True
USE_ARGV: bool = False
USE_RANDOM: bool = True
if USE_RANDOM:
	DEFAULT_VALUES_COUNT = 20
	DEFAULT_VALUES: List[int] = list(range(DEFAULT_VALUES_COUNT))
	random.shuffle(DEFAULT_VALUES)
else:
	DEFAULT_VALUES: List[int] = [7, 8, 4, 5, 3, 10, 9, 6, 1, 2]

def	argv_to_values(argv: List[str]) -> List[int]:
	return (list(map(int, sum(map(str.split, argv[1:]), []))))

def	check_values(values : List[int]) -> bool:
	if not values:
		eprint("There should be at least one value")
		return (False)
	if len(values) != len(set(values)):
		eprint("There are duplicate values in your input")
		return (False)
	return (True)

if __name__ == "__main__":
	values: List[int] = argv_to_values(sys.argv) if USE_ARGV else DEFAULT_VALUES
	if not check_values(values):
		exit(1)
	if values == sorted(values):
		exit(0)
	if USE_BINARY:
		_class = binary
		ctx: PushSwap[Binary] = PushSwap[Binary](list(map(Binary, values)), Binary)
	else:
		_class = ternary
		ctx: PushSwap[Ternary] = PushSwap[Ternary](list(map(Ternary, values)), Ternary)
	eprint(ctx, end='\n\n')
	_class.radix(ctx)
	eprint('\n', ctx, sep='', end='\n\n')
	_class.check_result(ctx)
