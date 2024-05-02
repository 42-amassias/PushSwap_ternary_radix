# Tri radix ternaire pour Push Swap

## Sujet

Push swap est un projet de [l'École 42](https://42.fr) dans lequel le sujet exige de trier une [pile](#pile) en utilisant deux [piles](#pile) (`A` et `B`).

Pour manipuler ces [piles](#pile), il existe 11 [instructions](#instructions).

---

## Instructions

- ### PA
	Empile l'élement au sommet de `B` sur `A` et dépile `B`.<br/>
	Si `B` est vide, ne fait rien.

	__Example__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	__Deviendra__:

	`A`: [ __`E3`__, `E1`, `E2` ]<br/>
	`B`: [ `E4`, `E5` ]

- ### PB
	Empile l'élement au sommet de `A` sur `B` et dépile `A`.<br/>
	Si `A` est vide, ne fait rien.

	__Example__:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	__Deviendra__:

	`A`: [ `E2` ]<br/>
	`B`: [ __`E1`__, `E3`, `E4`, `E5` ]

- ### SA
	Échange les deux premiers élements de `A`.<br/>
	Si `A` a moins de deux élements, ne fait rien.

	__Example__:

	`A`: [ __`E1`__, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	__Deviendra__:

	`A`: [ __`E2`__, __`E1`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ### SB
	Échange les deux premiers élements de `B`.<br/>
	Si `B` a moins de deux élements, ne fait rien.

	__Example__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, __`E4`__, `E5` ]

	__Deviendra__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E4`__, __`E3`__, `E5` ]

- ### SS
	Éxecute [`SA`](#sa) et [`SB`](#sb) simultanément.

	__Example__:

	`A`: [ __`E1`__, __`E2`__ ]<br/>
	`B`: [ __`E3`__, __`E4`__, `E5` ]

	__Deviendra__:

	`A`: [ __`E2`__, __`E1`__ ]<br/>
	`B`: [ __`E4`__, __`E3`__, `E5` ]

- ### RA
	Le premier élement de `A` deviens le dernier<br/>
	Si `A` est vide, ne fait rien.

	__Example__:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	__Deviendra__:

	`A`: [ `E2`, __`E1`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ### RB
	Le premier élement de `B` deviens le dernier<br/>
	Si `B` est vide, ne fait rien.

	__Example__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	__Deviendra__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ `E4`, `E5`, __`E3`__ ]

- ### RR
	Éxecute [`RA`](#ra) et [`RB`](#rb) simultanément.

	__Example__:

	`A`: [ __`E1`__, `E2` ]<br/>
	`B`: [ __`E3`__, `E4`, `E5` ]

	__Deviendra__:

	`A`: [ `E2`, __`E1`__ ]<br/>
	`B`: [ `E4`, `E5`, __`E3`__ ]

- ### RRA
	Le dernier élement de `A` deviens le premier<br/>
	Si `A` est vide, ne fait rien.

	__Example__:

	`A`: [ `E1`, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

	__Deviendra__:

	`A`: [ __`E2`__, `E1` ]<br/>
	`B`: [ `E3`, `E4`, `E5` ]

- ### RRB
	Le dernier élement de `B` deviens le premier<br/>
	Si `B` est vide, ne fait rien.

	__Example__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ `E3`, `E4`, __`E5`__ ]

	__Deviendra__:

	`A`: [ `E1`, `E2` ]<br/>
	`B`: [ __`E5`__, `E3`, `E4` ]

- ### RRR
	Éxecute [`RRA`](#rra) et [`RRB`](#rrb) simultanément.

	__Example__:

	`A`: [ `E1`, __`E2`__ ]<br/>
	`B`: [ `E3`, `E4`, __`E5`__ ]

	__Deviendra__:

	`A`: [ __`E2`__, `E1` ]<br/>
	`B`: [ __`E5`__, `E3`, `E4` ]

---

## Definitions

### Pile
Une pile est une structure de donnée qui ressemble à une liste dans laquelle on peut empiler (insérer) et dépiler (retirer) des élements mais seulement en pouvant acceder au dessus de cette pile.

__Example__:

1. On commence par une pile vide: `[]`
1. On y insert un élement `E1`: `[E1]`
1. Puis un deuxième élement `E2`: `[E2, E1]`
1. Puis un troisième `E3`: `[E3, E2, E1]`
1. On dépile: `[E2, E1]`.

L'élement clé à retenir: __Seul l'élement au sommet d'une pile est accessible.__
