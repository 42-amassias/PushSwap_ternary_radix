# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: amassias <amassias@student.42lehavre.fr    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/11/20 01:35:15 by amassias          #+#    #+#              #
#    Updated: 2024/05/02 10:58:29 by amassias         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

CC				:=	cc
NAME			:=	push_swap
THIRD_PARTY_DIR	:=	third-party
SRC_DIR			:=	src
INC_DIR			:=	include
BIN_DIR			:=	build

# **************************************************************************** #
#                                                                              #
# Third party libraries                                                        #
#                                                                              #
# **************************************************************************** #

LIB_FT_PATH		:=	$(THIRD_PARTY_DIR)/libft-full
LIB_FT			:=	$(LIB_FT_PATH)/libftfull.a

# **************************************************************************** #
#                                                                              #
# Compiler flags                                                               #
#                                                                              #
# **************************************************************************** #

CFLAGS			:=		\
	-I$(INC_DIR)		\
	-I$(LIB_FT_PATH)	\
	-Wall -Werror -Wextra -g
LFLAGS			:=		\
	-L$(LIB_FT_PATH)	\
	-lftfull

# **************************************************************************** #
#                                                                              #
# Files                                                                        #
#                                                                              #
# **************************************************************************** #

FILES			:=		\
	main stack/stack_create stack/stack_destroy stack/stack_iter			\
	stack/stack_peek stack/stack_pop stack/stack_push						\
	stack/stack_reverse_rotate stack/stack_rotate stack/stack_swap			\

SRCS			:=	$(addprefix $(SRC_DIR)/,$(addsuffix .c,$(FILES)))

OBJS			:=	$(addprefix $(BIN_DIR)/,$(addsuffix .o,$(FILES)))

# ############################################################################ #
#                                                                              #
# Terminal manipulations                                                       #
#                                                                              #
# ############################################################################ #

TERM_RESET			=	\033[0m
TERM_BLACK			=	\033[30m
TERM_RED			=	\033[31m
TERM_GREEN			=	\033[32m
TERM_YELLOW			=	\033[33m
TERM_BLUE			=	\033[34m
TERM_MAGENTA		=	\033[35m
TERM_CYAN			=	\033[36m
TERM_WHITE			=	\033[37m

TERM_UP				=	\033[1A
TERM_CLEAR_LINE		=	\033[2K\r

# **************************************************************************** #
#                                                                              #
# Phony rules                                                                  #
#                                                                              #
# **************************************************************************** #

.PHONY: all clean fclean re cleanlibs fcleanlibs _header _obj_header

all: $(NAME)

clean:
	@printf "$(TERM_YELLOW)Removing \"%s\"...\n$(TERM_RESET)" $(NAME)
	@rm -f $(OBJS)

fclean: clean
	@printf "$(TERM_YELLOW)Removing %d objects...\n$(TERM_RESET)" $(words $(OBJS))
	@rm -f $(NAME)

cleanlibs:
	@$(MAKE) clean -C $(LIB_FT_PATH)

fcleanlibs:
	@$(MAKE) fclean -C $(LIB_FT_PATH)

re:	fclean all

_header:
	@printf "$(TERM_GREEN)Welcome to $(TERM_BLUE)\"%s\"$(TERM_GREEN) builder !\n$(TERM_RESET)" $(NAME)

_obj_header:
	@printf "$(TERM_MAGENTA)Building objects$(TERM_RESET)...\n"

_obj_footer:
	@printf "$(TERM_UP)$(TERM_CLEAR_LINE)$(TERM_GREEN)Done building $(TERM_BLUE)%d$(TERM_GREEN) object(s) !\n$(TERM_RESET)" $(words $(OBJS))

# **************************************************************************** #
#                                                                              #
# Binary rules                                                                 #
#                                                                              #
# **************************************************************************** #

$(NAME): $(LIB_FT) _header _obj_header $(OBJS) _obj_footer
	@printf "$(TERM_MAGENTA)Making executable $(TERM_BLUE)\"%s\"$(TERM_MAGENTA)...$(TERM_RESET)" $@
	@$(CC) -o $@ $(OBJS) $(LFLAGS)
	@printf "$(TERM_CLEAR_LINE)$(TERM_GREEN)Done building $(TERM_BLUE)\"%s\"$(TERM_GREEN) !\n$(TERM_RESET)" $@

$(LIB_FT):
	@$(MAKE) -C $(LIB_FT_PATH)

$(BIN_DIR)/%.o: $(SRC_DIR)/%.c
	@printf "$(TERM_CLEAR_LINE)$(TERM_MAGENTA)Compiling $(TERM_BLUE)\"%s\"$(TERM_MAGENTA)...\n$(TERM_RESET)" $@
	@mkdir -p $(@D)
	@$(CC) -c $< -o $@ $(CFLAGS)
	@printf "$(TERM_UP)"
