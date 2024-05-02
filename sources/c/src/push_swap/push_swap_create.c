/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_create.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 12:49:29 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 17:46:25 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

#include <stdlib.h>

static int	_compare(
				void *a,
				void *b
				);

static bool	_normalize(
				t_push_swap *push_swap
				);

static bool	_create_stacks(
				t_push_swap *push_swap
				);

t_push_swap	*push_swap_create(
				size_t count,
				int values[count]
				)
{
	t_push_swap	*push_swap;

	if (count == 0)
		return (NULL);
	push_swap = malloc(
			sizeof(t_push_swap)
			+ (sizeof(t_list) + sizeof(int)) * count
			);
	if (push_swap == NULL)
		return (NULL);
	push_swap->a = (t_stack){0};
	push_swap->b = (t_stack){0};
	push_swap->silent = false;
	push_swap->value_count = count;
	ft_memcpy(&push_swap->values, values, sizeof(int) * count);
	if (_create_stacks(push_swap))
		return (push_swap_destroy(&push_swap), NULL);
	return (push_swap);
}

static int	_compare(
				void *a,
				void *b
				)
{
	return (**(int **)a - **(int **)b);
}

static bool	_normalize(
				t_push_swap *push_swap
				)
{
	int		**values;
	size_t	i;

	values = malloc(push_swap->value_count * sizeof(int *));
	if (values == NULL)
		return (true);
	i = 0;
	while (i < push_swap->value_count)
	{
		values[i] = &push_swap->values[i];
		++i;
	}
	ft_qsort(values, push_swap->value_count, sizeof(int *), _compare);
	i = 0;
	while (i < push_swap->value_count)
	{
		*values[i] = (int)i;
		++i;
	}
	free(values);
	return (false);
}

static bool	_create_stacks(
				t_push_swap *push_swap
				)
{
	t_list	*org;
	size_t	i;

	org = (t_list *)&push_swap->values[push_swap->value_count];
	i = 0;
	while (i < push_swap->value_count)
	{
		org[i] = (t_list){
			.next = org + i + 1,
			.content = &push_swap->values[i]
		};
		++i;
	}
	org[push_swap->value_count - 1].next = NULL;
	push_swap->a = (t_stack){
		.start = org,
		.end = ft_lstlast(org),
		.count = push_swap->value_count,
	};
	return (_normalize(push_swap));
}
