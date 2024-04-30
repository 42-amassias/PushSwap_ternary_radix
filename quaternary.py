import sys
import math
import utils

from typing import List
from push_swap import PushSwap
from utils import eprint
from functools import partial

from number import Quaternary

def	__check_result_header() -> None:
	W = 80
	utils.eprint_blue('#' * W)
	utils.eprint_blue('#', end=' ')
	utils.eprint_cyan('{:<{w}}'.format("Quaternary radix result checker".center(W - 4), w=W - 4), end=' ')
	utils.eprint_blue('#')
	utils.eprint_blue('#' * W)
	utils.eprint()

def	check_result(ctx: PushSwap[Quaternary]) -> None:
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

def	Quaternary_sort(ctx: PushSwap[Quaternary], N: int, silent: bool):
	def	_exec(instructions):
		[instruction() for instruction in instructions]

	def	_to_a1(_ctx: PushSwap[Quaternary], index: int):
		_exec({
			0: [_ctx.pa],
			1: [_ctx.pa, _ctx.ra],
			2: [_ctx.rb],
			3: [_ctx.rb],
			}[_ctx.peek_b()[index]])

	def	_to_b1(_ctx: PushSwap[Quaternary], index: int):
		_exec({
			0: [_ctx.pb],
			1: [_ctx.pb, _ctx.rb],
			2: [_ctx.ra],
			3: [_ctx.ra],
			}[_ctx.peek_a()[index]])

	def	_to_a2(_ctx: PushSwap[Quaternary], index: int):
		_exec({
			0: [],
			1: [],
			2: [_ctx.pa],
			3: [_ctx.pa, _ctx.ra],
			}[_ctx.peek_b()[index]])

	def	_to_b2(_ctx: PushSwap[Quaternary], index: int):
		_exec({
			0: [],
			1: [],
			2: [_ctx.pb],
			3: [_ctx.pb, _ctx.rb],
			}[_ctx.peek_a()[index]])

	ctx.set_silent(silent)
	odd = False
	for i in range(N):
		if odd:
			way1, way2, len = (_to_a1, _to_a2, ctx.get_b_len)
		else:
			way1, way2, len = (_to_b1, _to_b2, ctx.get_a_len)
		print(len())
		[way1(ctx, i) for _ in range(len())]
		[way2(ctx, i) for _ in range(len())]
		odd ^= True
	if not odd:
		return
	for _ in range(ctx.get_b_len()):
		ctx.pa()

def	__normalize(index: int, _: Quaternary, initial: List[Quaternary]=[], current: List[Quaternary]=[]):
	return (current[int(initial[index])])

def	radix(ctx: PushSwap[Quaternary]) -> None:
	N: int = math.ceil(math.log(len(ctx), Quaternary.get_base()))
	INITIAL_DISPOSITION = ctx.get_a()
	Quaternary_sort(ctx, N, True)
	ctx.remap(partial(__normalize, initial=INITIAL_DISPOSITION, current=ctx.get_a()))
	Quaternary_sort(ctx, N, False)
