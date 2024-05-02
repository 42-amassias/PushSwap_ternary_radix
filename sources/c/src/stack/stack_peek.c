/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_peek.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 15:10:01 by amassias          #+#    #+#             */
/*   Updated: 2024/05/01 15:39:27 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

#include <stdlib.h>

void	*stack_peek(
			t_stack *stack
			)
{
	if (stack->count == 0)
		return (NULL);
	return (stack->start->content);
}
