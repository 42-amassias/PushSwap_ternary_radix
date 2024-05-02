/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 14:44:24 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 18:02:56 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "algorithms.h"
#include "utils.h"

static int	*_query_values(
				int count,
				char *strings[count]
				);

int	main(int argc, char *argv[])
{
	t_push_swap	*ctx;
	int			*values;

	if (argc == 1)
		return (0);
	values = _query_values(argc - 1, argv + 1);
	if (values == NULL)
		return (1);
	ctx = push_swap_create(argc - 1, values);
	free(values);
	if (ctx == NULL)
		return (1);
	if (ternary_radix_sort(ctx))
		ft_fprintf(STDERR_FILENO, "An internal error occured.\n");
	push_swap_destroy(&ctx);
	return (0);
}

static int	*_query_values(
				int count,
				char *strings[count]
				)
{
	size_t	i;
	int		*values;

	values = malloc(count * sizeof(int));
	if (values == NULL)
		return (NULL);
	i = 0;
	while (i < (size_t) count)
	{
		values[i] = ft_atoi(strings[i]);
		++i;
	}
	return (values);
}
