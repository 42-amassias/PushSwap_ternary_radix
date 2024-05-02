# Push Swap's Ternary radix sort

## Subject
Push swap is a project from [École 42](https://42.fr) in which you have to sort a [stack](#stack) using two [stacks](#stack) (`A` and `B`).

To manipulate the [stacks](#stack), you have 11 available [instructions](#instructions).

---

## Instructions

- ### PA
	Pushes the top element of `B` onto `A`.<br/>
	If `B` is empty, does nothing.

	Exemple:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	Will become:

	`A`: [ __`E3`__, `E1`, `E2` ]<br/>
	`B`: [ `E4`, `E5` ]

- ### PB
	Pushes the top element of `A` onto `B`.<br/>
	If `A` is empty, does nothing.

	Exemple:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	Will become:

	`A`: [ `E2` ]<br/>
	`B`: [ __`E1`__, `E3`, `E4`, `E5` ]

- ### SA
	Swaps the two top elements of `A`.<br/>
	If `A` has less than two elements, does nothing.

	Exemple:

	`A`: [ __`E1`__, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	Will become:

	`A`: [ __`E2`__, __`E1`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ### SB
	Swaps the two top elements of `A`.<br/>
	If `A` has less than two elements, does nothing.

	Exemple:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, __`E4`__, `E5` ]

	Will become:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E4`__, __`E3`__, `E5` ]

- ### SS
	Does [`SA`](#sa) and [`SB`](#sb) simultaneously.

	Exemple:

	`A`: [ __`E1`__, __`E2`__ ]<br/>
	`B`: [ __`E3`__, __`E4`__, `E5` ]

	Will become:

	`A`: [ __`E2`__, __`E1`__ ]<br/>
	`B`: [ __`E4`__, __`E3`__, `E5` ]

- ### RA
	The first element of `A` becomes the last.<br/>
	If `A` is empty, does nothing.

	Exemple:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	Will become:

	`A`: [ `E2`, __`E1`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ### RB
	The first element of `B` becomes the last.<br/>
	If `B` is empty, does nothing.

	Exemple:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	Will become:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ `E4`, `E5`, __`E3`__ ]

- ### RR
	Does [`RA`](#ra) and [`RB`](#rb) simultaneously.

	Exemple:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	Will become:

	`A`: [ `E2`, __`E1`__ ]<br/>
	`B`: [ `E4`, `E5`, __`E3`__ ]

- ### RRA
	The last element of `A` becomes the first.<br/>
	If `A` is empty, does nothing.

	Exemple:

	`A`: [ `E1`, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	Will become:

	`A`: [ __`E2`__, `E1` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ### RRB
	The last element of `B` becomes the first.<br/>
	If `B` is empty, does nothing.

	Exemple:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ `E3`, `E4`, __`E5`__ ]

	Will become:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E5`__, `E3`, `E4` ]

- ### RRR
	Does [`RRA`](#rra) and [`RRB`](#rrb) simultaneously.

	Exemple:

	`A`: [ `E1`, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, __`E5`__ ]

	Will become:

	`A`: [ __`E2`__, `E1` ]<br/>
	`B`: [ __`E5`__, `E3`, `E4` ]

---

## Definitions

### Stack
A stack is a data structure which resembles a list in which you can push (insert) and pop (remove) elements except you can only access the top of the stack.

Exemple:

1. You start with an empty stack: `[]`.
1. Then you can push an element `E1` in it: `[E1]`
1. Then an other element `E2` in it: `[E2, E1]`
1. Why not a third `E3` in it: `[E3, E2, E1]`
1. Then you can pop: `[E2, E1]`.

The key element to remember is: __You can only touch the top of a stack.__