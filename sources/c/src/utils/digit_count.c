/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   digit_count.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 16:27:40 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 16:28:17 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "utils.h"

size_t	digit_count(
			unsigned int value,
			unsigned int base
			)
{
	if (value < base)
		return (1);
	return (1 + digit_count(value / base, base));
}
