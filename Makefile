# Directories
SRC_DIR = Examples
FAKE_HEADERS = ../pycparser-main/utils/fake_libc_include 

# Compilation variables
CC = gcc
CFLAGS = -E -nostdinc -I$(FAKE_HEADERS) 

# Target directory (can be overridden with make DIR=...)
DIR ?= $(SRC_DIR)

# Find ALL .c files recursively in target directory
SRCS = $(shell find $(DIR) -type f -name '*.c')
PREPROCESSED = $(SRCS:.c=.i)

# Default rule
all: preprocess

# Preprocess each .c file
%.i: %.c
	@echo "Preprocessing $<..."
	@mkdir -p $(dir $@)
	@$(CC) $(CFLAGS) -o "$@" "$<"

# Preprocess all files in specified directory
preprocess: $(PREPROCESSED)

# Clean only .i files in specified directory
clean:
	@echo "Cleaning *.i files in '$(DIR)'..."
	@find "$(DIR)" -type f -name '*.i' -delete
