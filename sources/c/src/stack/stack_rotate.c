/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_rotate.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 15:46:46 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 11:09:34 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

bool	stack_rotate(
			t_stack *stack
			)
{
	t_list	*head;

	if (stack->count < 2)
		return (false);
	head = stack->start;
	stack->start = head->next;
	stack->end = head;
	head->next = NULL;
	ft_lstadd_back(&stack->start, head);
	return (true);
}
