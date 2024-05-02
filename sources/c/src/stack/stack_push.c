/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_push.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 15:13:41 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 12:37:31 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

#include <stdlib.h>

void	__stack_push(
			t_stack *stack,
			t_list *node
			)
{
	ft_lstadd_front(&stack->start, node);
	if (stack->end == NULL)
		stack->end = node;
	++stack->count;
}

bool	stack_push(
			t_stack *stack,
			void *element
			)
{
	t_list	*node;

	if (element == NULL)
		return (false);
	node = ft_lstnew(element);
	if (node == NULL)
		return (false);
	__stack_push(stack, node);
	return (true);
}
