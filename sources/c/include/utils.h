/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   utils.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/02 16:26:05 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 17:10:22 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef UTILS_H
# define UTILS_H

# include <libft.h>
# include <sys/types.h>

size_t	digit_count(
			unsigned int value,
			unsigned int base
			);

void	*array_max(
			void *array,
			size_t nmemb,
			size_t size,
			t_comparator cmp
			);

int		compare_int(
			int *a,
			int *b
			);

int		get_digit(
			int value,
			size_t digit_index,
			size_t base
			);

void	*list_index(
			t_list *list,
			size_t index
			);

#endif