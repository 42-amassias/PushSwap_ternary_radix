import sys
import math
import utils

from push_swap import PushSwap
from utils import eprint

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
		eprint(',', end=' ')
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

def	radix(ctx: PushSwap[Ternary]):
	pass
