/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_push.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 13:23:47 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 13:46:57 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static bool	_push(
				t_stack *dst,
				t_stack *src
				);

void	push_swap_pa(
			t_push_swap *push_swap
			)
{
	if (_push(&push_swap->a, &push_swap->b) && !push_swap->silent)
		ft_printf("pa\n");
}

void	push_swap_pb(
			t_push_swap *push_swap
			)
{
	if (_push(&push_swap->b, &push_swap->a) && !push_swap->silent)
		ft_printf("pb\n");
}

static bool	_push(
				t_stack *dst,
				t_stack *src
				)
{
	if (src->count == 0)
		return (false);
	__stack_push(dst, __stack_pop(src));
	return (true);
}
