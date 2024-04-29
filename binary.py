import math
import utils

from utils import eprint
from push_swap import PushSwap

def	__check_result_header() -> None:
	W = 80
	utils.eprint_blue('#' * W)
	utils.eprint_blue('#', end=' ')
	utils.eprint_cyan('{:<{w}}'.format("Binary radix result checker".center(W - 4), w=W - 4), end=' ')
	utils.eprint_blue('#')
	utils.eprint_blue('#' * W)
	utils.eprint()

def	check_result(ctx: PushSwap[int]) -> None:
	l = ctx.get_a()
	N = math.ceil(math.log(len(ctx), 2))
	__check_result_header()
	for i, (v, s) in enumerate(zip(l, sorted(l))):
		eprint('[', i, ']', sep='', end=' ')
		eprint('Got', end=' ')
		for j in range(N):
			eprint(1 if (v & (1 << (N - j - 1))) else 0, end='')
		eprint('(', int(v), '),', sep='', end=' ')
		if v == s:
			utils.eprint_green('OK')
			continue

		utils.eprint_red('KO', end=': ')
		vstr = ''
		sstr = ''
		for j in range(N):
			index = N - j - 1 
			vd = 1 if (v & (1 << (N - index - 1))) else 0
			sd = 1 if (s & (1 << (N - index - 1))) else 0
			color = utils.TermColor.GREEN if vd == sd else utils.TermColor.RED
			vstr += color + str(vd)
			sstr += color + str(sd)
		vstr += utils.TermColor.RESET
		sstr += utils.TermColor.RESET
		eprint(vstr, '|', sstr)

def	radix(ctx: PushSwap[int]) -> None:
	digit_count: int = math.ceil(math.log2(ctx.get_element_count()))
	for i in range(digit_count):
		for _ in range(ctx.get_a_len()):
			ctx.pb() if (int(ctx.peek_a()) & (1 << i) == 0) else ctx.ra()
		for _ in range(ctx.get_b_len()):
			ctx.pa()