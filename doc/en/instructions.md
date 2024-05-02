# Instructions

[Go back to index](README.md)

---

- ## PA
	Pushes the top element of `B` onto `A`.<br/>
	If `B` is empty, does nothing.

	__Exemple__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	__Will become__:

	`A`: [ __`E3`__, `E1`, `E2` ]<br/>
	`B`: [ `E4`, `E5` ]

- ## PB
	Pushes the top element of `A` onto `B`.<br/>
	If `A` is empty, does nothing.

	__Exemple__:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	__Will become__:

	`A`: [ `E2` ]<br/>
	`B`: [ __`E1`__, `E3`, `E4`, `E5` ]

- ## SA
	Swaps the two top elements of `A`.<br/>
	If `A` has less than two elements, does nothing.

	__Exemple__:

	`A`: [ __`E1`__, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	__Will become__:

	`A`: [ __`E2`__, __`E1`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ## SB
	Swaps the two top elements of `A`.<br/>
	If `A` has less than two elements, does nothing.

	__Exemple__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, __`E4`__, `E5` ]

	__Will become__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E4`__, __`E3`__, `E5` ]

- ## SS
	Does [`SA`](#sa) and [`SB`](#sb) simultaneously.

	__Exemple__:

	`A`: [ __`E1`__, __`E2`__ ]<br/>
	`B`: [ __`E3`__, __`E4`__, `E5` ]

	__Will become__:

	`A`: [ __`E2`__, __`E1`__ ]<br/>
	`B`: [ __`E4`__, __`E3`__, `E5` ]

- ## RA
	The first element of `A` becomes the last.<br/>
	If `A` is empty, does nothing.

	__Exemple__:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	__Will become__:

	`A`: [ `E2`, __`E1`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ## RB
	The first element of `B` becomes the last.<br/>
	If `B` is empty, does nothing.

	__Exemple__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	__Will become__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ `E4`, `E5`, __`E3`__ ]

- ## RR
	Does [`RA`](#ra) and [`RB`](#rb) simultaneously.

	__Exemple__:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	__Will become__:

	`A`: [ `E2`, __`E1`__ ]<br/>
	`B`: [ `E4`, `E5`, __`E3`__ ]

- ## RRA
	The last element of `A` becomes the first.<br/>
	If `A` is empty, does nothing.

	__Exemple__:

	`A`: [ `E1`, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	__Will become__:

	`A`: [ __`E2`__, `E1` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ## RRB
	The last element of `B` becomes the first.<br/>
	If `B` is empty, does nothing.

	__Exemple__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ `E3`, `E4`, __`E5`__ ]

	__Will become__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E5`__, `E3`, `E4` ]

- ## RRR
	Does [`RRA`](#rra) and [`RRB`](#rrb) simultaneously.

	__Exemple__:

	`A`: [ `E1`, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, __`E5`__ ]

	__Will become__:

	`A`: [ __`E2`__, `E1` ]<br/>
	`B`: [ __`E5`__, `E3`, `E4` ]

---

[Go back to index](README.md)

---