/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_destroy.c                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 15:08:43 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 11:04:17 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

#include <stdio.h>

static void	_do_nothing(void *_);

void	stack_destroy(
			t_stack **stack_ptr
			)
{
	if (*stack_ptr == NULL)
		return ;
	ft_lstclear(&(*stack_ptr)->start, _do_nothing);
	free(*stack_ptr);
	*stack_ptr = NULL;
}

static void	_do_nothing(void *_)
{
	(void)_;
}
