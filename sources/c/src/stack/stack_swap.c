/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_swap.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 16:44:21 by amassias          #+#    #+#             */
/*   Updated: 2024/05/01 19:33:21 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

bool	stack_swap(
			t_stack *stack
			)
{
	if (stack->count < 2)
		return (false);
	ft_memswap(
		&stack->start->content,
		&stack->start->next->content,
		sizeof(void *)
		);
	return (true);
}
