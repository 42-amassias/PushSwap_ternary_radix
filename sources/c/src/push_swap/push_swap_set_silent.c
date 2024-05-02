/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap_set_silent.c                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 12:59:30 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 13:23:39 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	push_swap_set_silent(
			t_push_swap *push_swap,
			bool silent
			)
{
	push_swap->silent = silent;
}
