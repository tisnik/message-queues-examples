CC=gcc
LINKER=gcc

LIBS=nanomsg

CFLAGS=-O0 -Wall -ansi -pedantic
LFLAGS=-l$(LIBS)

LIBRARY_PATH=/usr/local/lib64/

.PHONY:	clean run_first run_second

all:	first second

%.o:	%.c
	$(CC) -c -o $@ $(CFLAGS) $<

first:	first.o
	$(CC) -o $@ $(LFLAGS) $<

second:	second.o
	$(CC) -o $@ $(LFLAGS) $<

clean:
	rm -f first.o \
	rm -f second.o \
	rm -f first \
	rm -f second

run_first:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./first

run_second:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./second
