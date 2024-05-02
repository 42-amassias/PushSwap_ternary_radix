/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_create.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 15:03:04 by amassias          #+#    #+#             */
/*   Updated: 2024/05/01 15:30:10 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "stack.h"

#include <stdlib.h>

t_stack	*stack_create(void)
{
	return ((t_stack *)ft_calloc(1, sizeof(t_stack)));
}
