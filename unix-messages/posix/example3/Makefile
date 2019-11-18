CC=gcc
LINKER=gcc

CFLAGS=-O0 -Wall -pedantic
LFLAGS=-lrt

.PHONY:	clean

all:	publisher subscriber

%.o:	%.c
	$(CC) -c -o $@ $(CFLAGS) $<

publisher:	publisher.o
	$(CC) -o $@ $< $(LFLAGS)

subscriber:	subscriber.o
	$(CC) -o $@ $< $(LFLAGS)

clean:
	rm -f *.o \
	rm -f publisher \
	rm -f subscriber
