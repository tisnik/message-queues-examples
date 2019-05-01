CC=gcc
LINKER=gcc

LIBS=nanomsg

CFLAGS=-O0 -Wall -ansi -pedantic
LFLAGS=-l$(LIBS)

LIBRARY_PATH=/usr/local/lib64/

.PHONY:	clean run_node1 run_node2

all:	node1 node2

%.o:	%.c
	$(CC) -c -o $@ $(CFLAGS) $<

node1:	node1.o
	$(CC) -o $@ $(LFLAGS) $<

node2:	node2.o
	$(CC) -o $@ $(LFLAGS) $<

clean:
	rm -f node1.o \
	rm -f node2.o \
	rm -f node1 \
	rm -f node2

run_node1:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./node1

run_node2:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./node2
