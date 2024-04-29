import sys
import math
import utils

from typing import List
from push_swap import PushSwap
from utils import eprint
from functools import partial

class Ternary:
	__value: int
	__digits: List[int]
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
	W = 80
	utils.eprint_blue('#' * W)
	utils.eprint_blue('#', end=' ')
	utils.eprint_cyan('{:<{w}}'.format("Ternary radix result checker".center(W - 4), w=W - 4), end=' ')
	utils.eprint_blue('#')
	utils.eprint_blue('#' * W)
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

def	ternary_sort(ctx: PushSwap[Ternary], N: int, silent: bool):
	def	_exec(instructions):
		[instruction() for instruction in instructions]

	def	_to_a(_ctx: PushSwap[Ternary], index: int):
		_exec({
			0: [_ctx.pa],
			1: [_ctx.pa, _ctx.ra],
			2: [_ctx.rb],
			}[_ctx.peek_b()[index]])

	def	_to_b(_ctx: PushSwap[Ternary], index: int):
		_exec({
			0: [_ctx.pb],
			1: [_ctx.pb, _ctx.rb],
			2: [_ctx.ra],
			}[_ctx.peek_a()[index]])

	ctx.set_silent(silent)
	odd = False
	for i in range(N):
		if odd:
			way, len, push = (_to_a, ctx.get_b_len, ctx.pa)
		else:
			way, len, push = (_to_b, ctx.get_a_len, ctx.pb)
		[way(ctx, i) for _ in range(len())]
		[push() for _ in range(len())]
		odd ^= True
	if not odd:
		return
	for _ in range(ctx.get_b_len()):
		ctx.pa()

def	__normalize(index: int, _: Ternary, initial: List[Ternary]=[], current: List[Ternary]=[]):
	return (current[int(initial[index])])

def	radix(ctx: PushSwap[Ternary]) -> None:
	N: int = math.ceil(math.log(len(ctx), 3))
	INITIAL_DISPOSITION = ctx.get_a()
	ternary_sort(ctx, N, True)
	ctx.remap(partial(__normalize, initial=INITIAL_DISPOSITION, current=ctx.get_a()))
	ternary_sort(ctx, N, False)
