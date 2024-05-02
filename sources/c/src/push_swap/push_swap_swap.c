/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_swap.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 13:43:38 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 13:55:12 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push_swap_sa(
			t_push_swap *push_swap
			)
{
	if (!stack_swap(&push_swap->a) && !push_swap->silent)
		ft_printf("sa\n");
}

void	push_swap_sb(
			t_push_swap *push_swap
			)
{
	if (!stack_swap(&push_swap->b) && !push_swap->silent)
		ft_printf("sb\n");
}

void	push_swap_ss(
			t_push_swap *push_swap
			)
{
	const bool	has_swapped_a = stack_swap(&push_swap->a);
	const bool	has_swapped_b = stack_swap(&push_swap->a);

	if (has_swapped_a && has_swapped_b)
	{
		if (!push_swap->silent)
			ft_printf("ss\n");
		return ;
	}
	if (has_swapped_a && !push_swap->silent)
		ft_printf("sa\n");
	if (has_swapped_b && !push_swap->silent)
		ft_printf("sb\n");
}
