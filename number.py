from typing import List

class Number:
	__base: int
	__value: int
	__digits: List[int]
	__digit_count: int

	def	__init__(self, base: int, value: int):
		self.__base = base
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
			length = decompose(n // self.__base) if n >= self.__base else 0
			self.__digits.append(n % self.__base)
			return (length + 1)

		self.__digit_count = decompose(self.__value)
		self.__digits.reverse()

	def	digit_count(self) -> int:
		return (self.__digit_count)

class Binary(Number):
	def	__init__(self, value: int):
		super().__init__(2, value)

class Ternary(Number):
	def	__init__(self, value: int):
		super().__init__(3, value)

class Quaternary(Number):
	def	__init__(self, value: int):
		super().__init__(4, value)
