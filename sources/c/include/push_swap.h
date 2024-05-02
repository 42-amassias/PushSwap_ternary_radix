/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 14:46:19 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 14:27:38 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef PUSH_SWAP_H
# define PUSH_SWAP_H

# include "stack.h"

typedef struct s_push_swap
{
	t_stack	a;
	t_stack	b;
	size_t	value_count;
	bool	silent;
	int		values[];
}	t_push_swap;

t_push_swap	*push_swap_create(
				size_t count,
				int values[count]
				);

void		push_swap_set_silent(
				t_push_swap *push_swap,
				bool silent
				);

void		push_swap_pa(
				t_push_swap *push_swap
				);

void		push_swap_pb(
				t_push_swap *push_swap
				);

void		push_swap_sa(
				t_push_swap *push_swap
				);

void		push_swap_sb(
				t_push_swap *push_swap
				);

void		push_swap_ss(
				t_push_swap *push_swap
				);

void		push_swap_ra(
				t_push_swap *push_swap
				);

void		push_swap_rb(
				t_push_swap *push_swap
				);

void		push_swap_rr(
				t_push_swap *push_swap
				);

void		push_swap_rra(
				t_push_swap *push_swap
				);

void		push_swap_rrb(
				t_push_swap *push_swap
				);

void		push_swap_rrr(
				t_push_swap *push_swap
				);

void		push_swap_destroy(
				t_push_swap **push_swap_ptr
				);

#endif
