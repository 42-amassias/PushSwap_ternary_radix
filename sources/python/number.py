from typing import List

class Number:
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
		if issubclass(type(o), Number):
			o = int(o)
		if type(o) is int:
			return (self.__value == o)
		return (False)

	def	__ne__(self, o) -> bool:
		if issubclass(type(o), Number):
			o = int(o)
		if type(o) is int:
			return (self.__value != o)
		return (False)

	def	__lt__(self, o) -> bool:
		if issubclass(type(o), Number):
			o = int(o)
		if type(o) is int:
			return (self.__value < o)
		return (False)

	def	__gt__(self, o) -> bool:
		if issubclass(type(o), Number):
			o = int(o)
		if type(o) is int:
			return (self.__value > o)
		return (False)

	def	__le__(self, o) -> bool:
		if issubclass(type(o), Number):
			o = int(o)
		if type(o) is int:
			return (self.__value <= o)
		return (False)

	def	__ge__(self, o) -> bool:
		if issubclass(type(o), Number):
			o = int(o)
		if type(o) is int:
			return (self.__value >= o)
		return (False)

	def	__hash__(self):
		return (self.__value.__hash__())

	def	__decompose(self) -> None:
		def	decompose(n: int) -> int:
			length = decompose(n // self.__class__.get_base()) if n >= self.__class__.get_base() else 0
			self.__digits.append(n % self.__class__.get_base())
			return (length + 1)
		self.__digit_count = decompose(self.__value)
		self.__digits.reverse()

	def	digit_count(self) -> int:
		return (self.__digit_count)

	@staticmethod
	def	get_base() -> int:
		raise NotImplementedError("Please Implement this method")

class Binary(Number):
	def	get_base() -> int:
		return (2)

class Ternary(Number):
	def	get_base() -> int:
		return (3)

class Quaternary(Number):
	def	get_base() -> int:
		return (4)