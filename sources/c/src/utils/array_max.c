/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   array_max.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 16:28:29 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 17:19:58 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "utils.h"

void	*array_max(
			void *_array,
			size_t nmemb,
			size_t size,
			t_comparator cmp
			)
{
	char	*array;
	void	*max;
	size_t	i;

	if (nmemb == 0 || size == 0)
		return (NULL);
	array = _array + size;
	max = _array;
	i = 1;
	while (i++ < nmemb)
	{
		if (cmp(array, max) > 0)
			max = array;
		array += size;
	}
	return (max);
}
