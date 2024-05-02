/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ternary_radix_sort.c                               :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 14:05:14 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 18:01:59 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"
#include "utils.h"

static void	_a_to_b(
				t_push_swap *ctx,
				size_t digit_index
				);

static void	_b_to_a(
				t_push_swap *ctx,
				size_t digit_index
				);

static bool	_normalize(
				t_push_swap *ctx
				);

static void	_sort(
				t_push_swap *ctx,
				size_t digit_count
				);

bool	ternary_radix_sort(
			t_push_swap *ctx
			)
{
	int	max;
	int	dc;

	max = *(int *)array_max(
			ctx->values,
			ctx->value_count,
			sizeof(int),
			(t_comparator)compare_int
			);
	dc = digit_count(max, 3);
	push_swap_set_silent(ctx, true);
	_sort(ctx, dc);
	if (_normalize(ctx))
		return (true);
	push_swap_set_silent(ctx, false);
	_sort(ctx, dc);
	return (false);
}

static void	_a_to_b(
				t_push_swap *ctx,
				size_t digit_index
				)
{
	const size_t	n = ctx->a.count;
	int				digit;
	size_t			i;

	i = 0;
	while (i++ < n)
	{
		digit = get_digit(*(int *)stack_peek(&ctx->a), digit_index, 3);
		if (digit == 0)
			push_swap_pb(ctx);
		else if (digit == 1)
		{
			push_swap_pb(ctx);
			push_swap_rb(ctx);
		}
		else
			push_swap_ra(ctx);
	}
}

static void	_b_to_a(
				t_push_swap *ctx,
				size_t digit_index
				)
{
	const size_t	n = ctx->b.count;
	int				digit;
	size_t			i;

	i = 0;
	while (i++ < n)
	{
		digit = get_digit(*(int *)stack_peek(&ctx->b), digit_index, 3);
		if (digit == 0)
			push_swap_pa(ctx);
		else if (digit == 1)
		{
			push_swap_pa(ctx);
			push_swap_ra(ctx);
		}
		else
			push_swap_rb(ctx);
	}
}

static bool	_normalize(
				t_push_swap *ctx
				)
{
	int		*result;
	size_t	i;

	i = 0;
	result = malloc(ctx->value_count * sizeof(int));
	if (result == NULL)
		return (true);
	while (i < ctx->value_count)
	{
		result[i] = *(int *)list_index(ctx->a.start, ctx->values[i]);
		++i;
	}
	i = 0;
	while (i < ctx->value_count)
	{
		*(int *)list_index(ctx->a.start, i) = result[i];
		++i;
	}
	free(result);
	return (false);
}

static void	_sort(
				t_push_swap *ctx,
				size_t digit_count
				)
{
	size_t	i;

	i = 0;
	while (i < digit_count)
	{
		if (i % 2)
		{
			_b_to_a(ctx, i);
			while (ctx->b.count)
				push_swap_pa(ctx);
		}
		else
		{
			_a_to_b(ctx, i);
			while (ctx->a.count)
				push_swap_pb(ctx);
		}
		++i;
	}
	if (digit_count % 2 == 0)
		return ;
	while (ctx->b.count)
		push_swap_pa(ctx);
}
