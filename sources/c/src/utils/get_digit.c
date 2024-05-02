/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_digit.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 17:10:32 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 17:20:35 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "utils.h"

int	get_digit(
		int value,
		size_t digit_index,
		size_t base
		)
{
	if (digit_index == 0)
		return (value % base);
	return (get_digit(value / base, digit_index - 1, base));
}
