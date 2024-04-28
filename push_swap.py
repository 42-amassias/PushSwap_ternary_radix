from typing import Generic, Type, TypeVar, List, Deque
from collections import deque
import utils

T = TypeVar("T")

class PushSwap(Generic[T]):
	__type			:	Type[T]
	__a				:	Deque[T]
	__b				:	Deque[T]
	__element_count	:	int
	__a_length		:	int
	__b_length		:	int

	def	__init__(self, initial_config: List[T], _type: Type[T]):
		self.__type = _type
		self.__element_count = len(initial_config)
		self.__a_length = self.__element_count
		self.__b_length = 0
		self.__a = deque[T](initial_config)
		self.__b = deque[T]()
		self.__normalize()

	def	__str__(self) -> str:
		def	stack_to_str(name : str, stack: Deque[T]) -> str:
			s = ' '.join(map(str, stack))
			return (name + ": " + (s if s else "Empty"))

		a = stack_to_str("a", self.__a)
		b = stack_to_str("b", self.__b)
		return (a + "\n" + b)

	def	__len__(self) -> int:
		return (self.__element_count)

	def	__normalize(self) -> None:
		l = map(utils.fst, sorted(enumerate(self.__a), key=utils.snd))
		l = map(utils.fst, sorted(enumerate(l), key=utils.snd))
		self.__a = deque[T](map(self.__type, l))

	def	__push(self, dest: Deque[T], src: Deque[T]) -> bool:
		if not src:
			return (False)
		dest.appendleft(src.popleft())
		return (True)

	def	__swap(self, stack: Deque[T]) -> bool:
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

	def	__rotate(self, stack: Deque[T]) -> bool:
		if not stack:
			return (False)
		stack.rotate(-1)
		return (True)

	def	__reverse_rotate(self, stack: Deque[T]) -> bool:
		if not stack:
			return (False)
		stack.rotate(1)
		return (True)

	def	__peek(self, stack: Deque[T]) -> T | None:
		if not stack:
			return (None)
		return (stack[0])

	def	pa(self) -> None:
		if not self.__push(self.__a, self.__b):
			return
		self.__a_length = self.__a_length + 1
		self.__b_length = self.__b_length - 1
		print("pa")

	def	pb(self) -> None:
		if not self.__push(self.__b, self.__a):
			return
		self.__a_length = self.__a_length - 1
		self.__b_length = self.__b_length + 1
		print("pb")
	
	def	sa(self) -> None:
		if not self.__swap(self.__a):
			return
		print("sa")

	def	sb(self) -> None:
		if not self.__swap(self.__b):
			return
		print("sb")

	def	ra(self) -> None:
		if self.__a_length < 2 or not self.__rotate(self.__a):
			return
		print("ra")

	def	rb(self) -> None:
		if self.__b_length < 2 or not self.__rotate(self.__b):
			return
		print("rb")

	def	rra(self) -> None:
		if self.__a_length < 2 or not self.__reverse_rotate(self.__a):
			return
		print("rra")

	def	rrb(self) -> None:
		if self.__b_length < 2 or not self.__reverse_rotate(self.__b):
			return
		print("rrb")

	def	peek_a(self) -> T:
		return (self.__peek(self.__a))

	def	peek_b(self) -> T:
		return (self.__peek(self.__b))

	def	get_a(self) -> List[T]:
		return (list(self.__a))

	def	get_b(self) -> List[T]:
		return (list(self.__b))

	def	get_a_len(self) -> int:
		return (self.__a_length)

	def	get_b_len(self) -> int:
		return (self.__b_length)

	def	get_element_count(self) -> int:
		return (self.__element_count)
