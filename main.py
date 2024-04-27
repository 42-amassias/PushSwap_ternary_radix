#!/usr/bin/python3

from push_swap import PushSwap

if __name__ == "__main__":
	ps = PushSwap[int]([1, 2, 3])
	print(ps, end='\n\n')

	ps.sa()
	print(ps, end='\n\n')
