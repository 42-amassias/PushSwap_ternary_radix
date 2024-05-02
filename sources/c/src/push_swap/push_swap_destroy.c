/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_destroy.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 12:56:42 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 12:59:02 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

#include <stdlib.h>

void	push_swap_destroy(
			t_push_swap **push_swap_ptr
			)
{
	t_stack	*stack;

	if (*push_swap_ptr == NULL)
		return ;
	((void)0, stack = &(*push_swap_ptr)->a, stack_destroy(&stack));
	((void)0, stack = &(*push_swap_ptr)->b, stack_destroy(&stack));
	free(*push_swap_ptr);
	*push_swap_ptr = NULL;
}
