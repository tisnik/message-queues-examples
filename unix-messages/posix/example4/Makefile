CC=gcc
LINKER=gcc

CFLAGS=-O0 -Wall -pedantic
LFLAGS=-lrt

.PHONY:	clean

all:	publisher subscriber create

%.o:	%.c
	$(CC) -c -o $@ $(CFLAGS) $<

create:	create.o
	$(CC) -o $@ $< $(LFLAGS)

publisher:	publisher.o
	$(CC) -o $@ $< $(LFLAGS)

subscriber:	subscriber.o
	$(CC) -o $@ $< $(LFLAGS)

clean:
	rm -f *.o \
	rm -f publisher \
	rm -f subscriber \
	rm -f create
