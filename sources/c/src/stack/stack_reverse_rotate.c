/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_reverse_rotate.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 15:39:12 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 11:14:27 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

bool	stack_reverse_rotate(
			t_stack *stack
			)
{
	t_list	*end;
	t_list	**itr;

	if (stack->count < 2)
		return (false);
	itr = &stack->start;
	while ((*itr)->next->next)
		itr = &(*itr)->next;
	end = (*itr)->next;
	stack->end = *itr;
	stack->end->next = NULL;
	(*itr)->next = NULL;
	ft_lstadd_front(&stack->start, end);
	return (true);
}
