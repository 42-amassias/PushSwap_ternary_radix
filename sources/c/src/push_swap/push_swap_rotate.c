/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_rotate.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 13:53:04 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 13:56:52 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push_swap_ra(
			t_push_swap *push_swap
			)
{
	if (stack_rotate(&push_swap->a) && !push_swap->silent)
		ft_printf("ra\n");
}

void	push_swap_rb(
			t_push_swap *push_swap
			)
{
	if (stack_rotate(&push_swap->b) && !push_swap->silent)
		ft_printf("rb\n");
}

void	push_swap_rr(
			t_push_swap *push_swap
			)
{
	const bool	has_rotated_a = stack_rotate(&push_swap->a);
	const bool	has_rotated_b = stack_rotate(&push_swap->a);

	if (has_rotated_a && has_rotated_b)
	{
		if (!push_swap->silent)
			ft_printf("rr\n");
		return ;
	}
	if (has_rotated_a && !push_swap->silent)
		ft_printf("ra\n");
	if (has_rotated_b && !push_swap->silent)
		ft_printf("rb\n");
}
