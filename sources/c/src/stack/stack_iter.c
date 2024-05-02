/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_iter.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 18:53:11 by amassias          #+#    #+#             */
/*   Updated: 2024/05/01 18:54:23 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

void	stack_iter(
			t_stack *stack,
			void (*fun)(void *)
			)
{
	t_list	*list;

	if (stack == NULL)
		return ;
	list = stack->start;
	while (list)
	{
		fun(list->content);
		list = list->next;
	}
}
