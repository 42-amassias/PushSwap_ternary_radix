/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 14:44:24 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 19:05:42 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "algorithms.h"
#include "utils.h"

#include <limits.h>

static bool	_parse_and_check_int(
				const char *str,
				int	*res
				);

static bool	_has_duplicate_values(
				const int *values,
				size_t count
				);

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

static bool	_parse_and_check_int(
				const char *str,
				int	*res
				)
{
	long	value;
	int		sign;

	value = 0;
	sign = 1;
	while (ft_isspace(*str))
		++str;
	if (*str == '-' || *str == '+')
	{
		if (*str == '-')
			sign = -sign;
		++str;
	}
	if (!ft_isdigit(*str))
		return (false);
	while (ft_isdigit(*str))
	{
		value = 10 * value + (*str++) - '0';
		if (sign * value > INT_MAX || sign * value < INT_MIN)
			return (false);
	}
	while (ft_isspace(*str))
		++str;
	*res = (int) sign * value;
	return (*str == '\0');
}

static bool	_has_duplicate_values(
				const int *values,
				size_t count
				)
{
	size_t	i;
	size_t	j;

	i = 0;
	while (i < count - 1)
	{
		j = i + 1;
		while (j < count)
		{
			if (values[i] == values[j])
			{
				ft_fprintf(STDERR_FILENO,
					"Values are duplicated: Indices %u and %u (%d)\n",
					(unsigned int) i,
					(unsigned int) j,
					values[i]
					);
				return (true);
			}
			++j;
		}
		++i;
	}
	return (false);
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
		if (!_parse_and_check_int(strings[i], &values[i]))
		{
			ft_fprintf(STDERR_FILENO, "Invalid value (index %u): %s\n",
				(unsigned int) i,
				strings[i]
				);
			free(values);
			return (NULL);
		}
		++i;
	}
	if (_has_duplicate_values(values, count))
		(free(values), values = NULL);
	return (values);
}
