/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_pop.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 15:10:55 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 12:38:21 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

#include <stdlib.h>

t_list	*__stack_pop(
			t_stack *stack
			)
{
	t_list	*head;

	if (stack->count == 0)
		return (NULL);
	head = stack->start;
	--stack->count;
	stack->start = stack->start->next;
	if (stack->start == NULL)
		stack->end = NULL;
	head->next = NULL;
	return (head);
}

void	*stack_pop(
			t_stack *stack
			)
{
	t_list	*node;
	void	*element;

	node = __stack_pop(stack);
	if (node == NULL)
		return (NULL);
	element = node->content;
	free(node);
	return (element);
}
