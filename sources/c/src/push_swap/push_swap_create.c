/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_create.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 12:49:29 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 12:56:27 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

#include <stdlib.h>

t_push_swap	*push_swap_create(
				size_t count,
				int values[count]
				)
{
	t_push_swap	*push_swap;

	if (count == 0)
		return (NULL);
	push_swap = malloc(sizeof(t_push_swap) + sizeof(int) * count);
	if (push_swap == NULL)
		return (NULL);
	*push_swap = (t_push_swap){
		.a = (t_stack){0},
		.b = (t_stack){0},
		.silent = false,
		.value_count = count
	};
	ft_memcmp(&push_swap->values, values, sizeof(int) * count);
	return (push_swap);
}
