from typing import Generic, TypeVar
from collections import deque
import utils

T = TypeVar("T")

class PushSwap(Generic[T]):
	__a: deque[T]
	__b: deque[T]

	def	__init__(self, initial_config: list[T]):
		self.__a = deque(initial_config)
		self.__b = deque()
		self.__normalize()

	def	__str__(self) -> str:
		def	stack_to_str(name : str, stack: deque[T]) -> str:
			s = ' '.join(map(str, stack))
			return (name + ": " + (s if s else "Empty"))

		a = stack_to_str("a", self.__a)
		b = stack_to_str("b", self.__b)
		return (a + "\n" + b)

	def	__normalize(self) -> None:
		self.__a = deque(map(utils.fst, sorted(enumerate(map(utils.fst, sorted(enumerate(self.__a), key=utils.snd))), key=utils.snd)))

	def	__push(self, dest: deque[T], src: deque[T]) -> bool:
		if not src:
			return (False)
		dest.appendleft(src.popleft())
		return (True)

	def	__swap(self, stack: deque[T]) -> bool:
		if not stack:
			return (False)
		first = stack.popleft()
		if not stack:
			stack.appendleft(first)
			return (False)
		second = stack.popleft()
		stack.appendleft(first)
		stack.appendleft(second)
		return (True)

	def	__rotate(self, stack: deque[T]) -> bool:
		if not stack:
			return (False)
		stack.rotate(-1)
		return (True)

	def	__reverse_rotate(self, stack: deque[T]) -> bool:
		if not stack:
			return (False)
		stack.rotate(1)
		return (True)

	def	__peek(self, stack: deque[T]) -> T | None:
		if not stack:
			return (None)
		return (stack[0])

	def	pa(self) -> None:
		if self.__push(self.__a, self.__b):
			print("pa")

	def	pb(self) -> None:
		if self.__push(self.__b, self.__a):
			print("pb")
	
	def	sa(self) -> None:
		if self.__swap(self.__a):
			print("sa")

	def	sb(self) -> None:
		if self.__swap(self.__b):
			print("sb")

	def	ra(self) -> None:
		if self.__rotate(self.__a):
			print("ra")

	def	rb(self) -> None:
		if self.__rotate(self.__b):
			print("rb")

	def	rra(self) -> None:
		if self.__reverse_rotate(self.__a):
			print("rra")

	def	rrb(self) -> None:
		if self.__reverse_rotate(self.__b):
			print("rrb")

	def	peek_a(self) -> T | None:
		return (self.__peek(self.__a))

	def	peek_b(self) -> T | None:
		return (self.__peek(self.__b))

	def	get_a(self) -> list[T]:
		return (list(self.__a))
	
	def	get_b(self) -> list[T]:
		return (list(self.__b))
