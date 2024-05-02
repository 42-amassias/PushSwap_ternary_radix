/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_reverse_rotate.c                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 13:58:00 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 13:58:38 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push_swap_rra(
			t_push_swap *push_swap
			)
{
	if (stack_reverse_rotate(&push_swap->a) && !push_swap->silent)
		ft_printf("rra\n");
}

void	push_swap_rrb(
			t_push_swap *push_swap
			)
{
	if (stack_reverse_rotate(&push_swap->b) && !push_swap->silent)
		ft_printf("rrb\n");
}

void	push_swap_rrr(
			t_push_swap *push_swap
			)
{
	const bool	has_rotated_a = stack_reverse_rotate(&push_swap->a);
	const bool	has_rotated_b = stack_reverse_rotate(&push_swap->a);

	if (has_rotated_a && has_rotated_b)
	{
		if (!push_swap->silent)
			ft_printf("rrr\n");
		return ;
	}
	if (has_rotated_a && !push_swap->silent)
		ft_printf("rra\n");
	if (has_rotated_b && !push_swap->silent)
		ft_printf("rrb\n");
}
