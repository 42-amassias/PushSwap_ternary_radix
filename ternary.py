class Ternary:
	__value: int
	__digits: list[int]
	__digit_count: int

	def	__init__(self, value: int):
		self.__value = value
		self.__digits = []
		self.__decompose()

	def	__getitem__(self, key: int) -> int:
		if key < 0 or key >= self.__digit_count:
			return None
		return (self.__digits[key])

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
