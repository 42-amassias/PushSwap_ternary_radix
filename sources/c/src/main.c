/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 14:44:24 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 14:32:34 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

#define N 5

void	print_ctx(t_push_swap *ctx)
{
	t_list	*itr;

	ft_printf("a: ");
	itr = ctx->a.start;
	while (itr)
	{
		ft_printf("%d ", *(const int *)itr->content);
		itr = itr->next;
	}
	ft_printf("\n");
	ft_printf("b: ");
	itr = ctx->b.start;
	while (itr)
	{
		ft_printf("%d ", *(const int *)itr->content);
		itr = itr->next;
	}
	ft_printf("\n");
}

int	main(void)
{
	const int	values[N] = {2, 4, 0, 1, 3};
	t_push_swap	*ctx;

	ctx = push_swap_create(N, (int *)values);
	if (ctx == NULL)
		return (1);
	print_ctx(ctx);
	ft_printf("\n");
	push_swap_pa(ctx);
	print_ctx(ctx);
	ft_printf("\n");
	push_swap_pb(ctx);
	print_ctx(ctx);
	ft_printf("\n");
	push_swap_destroy(&ctx);
	return (0);
}
