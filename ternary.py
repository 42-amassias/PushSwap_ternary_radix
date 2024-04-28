import sys
import math
import utils

from typing import List
from push_swap import PushSwap
from utils import eprint
from functools import partial

class Ternary:
	__value: int
	__digits: list[int]
	__digit_count: int

	def	__init__(self, value: int):
		self.__value = value
		self.__digits = []
		self.__decompose()

	def	__getitem__(self, key: int) -> int:
		if key < 0:
			return None
		return (self.__digits[key] if key < self.__digit_count else 0)

	def	__str__(self):
		return (''.join(map(str, reversed(self.__digits))))

	def	__int__(self) -> int:
		return (self.__value)

	def	__eq__(self, o) -> bool:
		if type(o) is Ternary:
			o = int(o)
		if type(o) is int:
			return (self.__value == o)
		return (False)

	def	__ne__(self, o) -> bool:
		if type(o) is Ternary:
			o = int(o)
		if type(o) is int:
			return (self.__value != o)
		return (False)

	def	__lt__(self, o) -> bool:
		if type(o) is Ternary:
			o = int(o)
		if type(o) is int:
			return (self.__value < o)
		return (False)

	def	__gt__(self, o) -> bool:
		if type(o) is Ternary:
			o = int(o)
		if type(o) is int:
			return (self.__value > o)
		return (False)

	def	__le__(self, o) -> bool:
		if type(o) is Ternary:
			o = int(o)
		if type(o) is int:
			return (self.__value <= o)
		return (False)

	def	__ge__(self, o) -> bool:
		if type(o) is Ternary:
			o = int(o)
		if type(o) is int:
			return (self.__value >= o)
		return (False)

	def	__hash__(self):
		return (self.__value.__hash__())

	def	__decompose(self) -> None:
		def	decompose(n: int) -> int:
			length = decompose(n // 3) if n >= 3 else 0
			self.__digits.append(n % 3)
			return (length + 1)

		self.__digit_count = decompose(self.__value)
		self.__digits.reverse()

	def	digit_count(self) -> int:
		return (self.__digit_count)

def	__check_result_header() -> None:
	utils.eprint_blue('#'*80)
	utils.eprint_blue('#', end=' ')
	utils.eprint_cyan('{:<76}'.format("Ternary radix result checker".center(76)), end=' ')
	utils.eprint_blue('#')
	utils.eprint_blue('#'*80)
	utils.eprint()

def	check_result(ctx: PushSwap[Ternary]) -> None:
	l = ctx.get_a()
	N = math.ceil(math.log(len(ctx), 3))
	__check_result_header()
	for i, (v, s) in enumerate(zip(l, sorted(l))):
		eprint('[', i, ']', sep='', end=' ')
		eprint('Got', end=' ')
		for j in range(N):
			eprint(v[N - j - 1], end='')
		eprint('(', int(v), '),', sep='', end=' ')
		if v == s:
			utils.eprint_green('OK')
			continue

		utils.eprint_red('KO', end=': ')
		vstr = ''
		sstr = ''
		for j in range(N):
			index = N - j - 1 
			vd = v[index]
			sd = s[index]
			color = utils.TermColor.GREEN if vd == sd else utils.TermColor.RED
			vstr += color + str(vd)
			sstr += color + str(sd)
		vstr += utils.TermColor.RESET
		sstr += utils.TermColor.RESET
		eprint(vstr, '|', sstr)

def	ternary_sort(ctx: PushSwap[Ternary], N: int):
	odd = False
	for i in range(N):
		if odd:
			OPS = (PushSwap.peek_b, PushSwap.pa, PushSwap.ra, PushSwap.rb, PushSwap.get_b_len)
		else:
			OPS = (PushSwap.peek_a, PushSwap.pb, PushSwap.rb, PushSwap.ra, PushSwap.get_a_len)
		for _ in range(OPS[4](ctx)):
			digit: int = OPS[0](ctx)[i]
			if digit == 0:
				OPS[1](ctx)
			elif digit == 1:
				OPS[1](ctx)
				OPS[2](ctx)
			else: # digit == 2
				OPS[3](ctx)
		for _ in range(OPS[4](ctx)):
			OPS[1](ctx)
		odd ^= True
	if odd:
		for _ in range(ctx.get_b_len()):
			ctx.pa()

def	normalize(index: int, value: Ternary, initial: List[Ternary]=[], current: List[Ternary]=[]):
	return (current[int(initial[index])])

def	radix(ctx: PushSwap[Ternary]) -> None:
	N: int = math.ceil(math.log(len(ctx), 3))
	ctx.set_silent(True)
	INITIAL_DISPOSITION = ctx.get_a()
	ternary_sort(ctx, N)
	ctx.remap(partial(normalize, initial=INITIAL_DISPOSITION, current=ctx.get_a()))
	ctx.set_silent(False)
	ternary_sort(ctx, N)
