import sys
from functools import partial

class TermColor:
	RED='\033[91m'
	GREEN='\033[92m'
	YELLOW='\033[93m'
	BLUE='\033[94m'
	PURPLE='\033[95m'
	CYAN='\033[96m'
	WHITE='\033[97m'
	RESET='\033[0m'

def	fst(x):
	return (x[0])

def	snd(x):
	return (x[1])

# def	eprint():
# 	pass

eprint = partial(print, file=sys.stderr)

def	print_col(msg: str, color: str='', sep: str=' ', end: str='\n', file=sys.stderr) -> None:
	print(color + msg + TermColor.RESET, sep=sep, end=end, file=file)

def	print_green(msg: str, sep: str=' ', end: str='\n', file=sys.stdout) -> None:
	print_col(msg, TermColor.GREEN, sep, end, file)

def	print_red(msg: str, sep: str=' ', end: str='\n', file=sys.stdout) -> None:
	print_col(msg, TermColor.RED, sep, end, file)

def	print_yellow(msg: str, sep: str=' ', end: str='\n', file=sys.stdout) -> None:
	print_col(msg, TermColor.YELLOW, sep, end, file)

def	print_blue(msg: str, sep: str=' ', end: str='\n', file=sys.stdout) -> None:
	print_col(msg, TermColor.BLUE, sep, end, file)

def	print_purple(msg: str, sep: str=' ', end: str='\n', file=sys.stdout) -> None:
	print_col(msg, TermColor.PURPLE, sep, end, file)

def	print_cyan(msg: str, sep: str=' ', end: str='\n', file=sys.stdout) -> None:
	print_col(msg, TermColor.CYAN, sep, end, file)

def	print_white(msg: str, sep: str=' ', end: str='\n', file=sys.stdout) -> None:
	print_col(msg, TermColor.WHITE, sep, end, file)

def	eprint_green(msg: str, sep: str=' ', end: str='\n') -> None:
	print_col(msg, TermColor.GREEN, sep, end, sys.stderr)

def	eprint_red(msg: str, sep: str=' ', end: str='\n') -> None:
	print_col(msg, TermColor.RED, sep, end, sys.stderr)

def	eprint_yellow(msg: str, sep: str=' ', end: str='\n') -> None:
	print_col(msg, TermColor.YELLOW, sep, end, sys.stderr)

def	eprint_blue(msg: str, sep: str=' ', end: str='\n') -> None:
	print_col(msg, TermColor.BLUE, sep, end, sys.stderr)

def	eprint_purple(msg: str, sep: str=' ', end: str='\n') -> None:
	print_col(msg, TermColor.PURPLE, sep, end, sys.stderr)

def	eprint_cyan(msg: str, sep: str=' ', end: str='\n') -> None:
	print_col(msg, TermColor.CYAN, sep, end, sys.stderr)

def	eprint_white(msg: str, sep: str=' ', end: str='\n') -> None:
	print_col(msg, TermColor.WHITE, sep, end, sys.stderr)
