import math

from push_swap import PushSwap

def	binary_radix(ctx: PushSwap[int]) -> None:
	digit_count: int = math.ceil(math.log2(ctx.get_element_count()))
	for i in range(digit_count):
		for _ in range(ctx.get_a_len()):
			ctx.pb() if (int(ctx.peek_a()) & (1 << i) == 0) else ctx.ra()
		for _ in range(ctx.get_b_len()):
			ctx.pa()