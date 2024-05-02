/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   list_index.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 17:01:14 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 17:02:05 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "utils.h"

void	*list_index(
			t_list *list,
			size_t index
			)
{
	if (list == NULL)
		return (NULL);
	if (index == 0)
		return (list->content);
	return (list_index(list->next, index - 1));
}
