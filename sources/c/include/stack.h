/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack.h                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2024/05/01 14:52:12 by amassias          #+#    #+#             */
/*   Updated: 2024/05/02 12:33:46 by amassias         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef STACK_H
# define STACK_H

# include "libft.h"

# include <sys/types.h>
# include <stdbool.h>

typedef struct s_stack
{
	size_t	count;
	t_list	*start;
	t_list	*end;
}	t_stack;

t_stack	*stack_create(void);

void	*stack_peek(
			t_stack *stack
			);

t_list	*__stack_pop(
			t_stack *stack
			);

void	*stack_pop(
			t_stack *stack
			);

void	__stack_push(
			t_stack *stack,
			t_list *node
			);

bool	stack_push(
			t_stack *stack,
			void *element
			);

bool	stack_rotate(
			t_stack *stack
			);

bool	stack_reverse_rotate(
			t_stack *stack
			);

bool	stack_swap(
			t_stack *stack
			);

void	stack_iter(
			t_stack *stack,
			void (*fun)(void *)
			);

void	stack_destroy(
			t_stack **stack_ptr
			);

#endif