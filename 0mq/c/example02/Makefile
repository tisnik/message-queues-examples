CC=gcc
LINKER=gcc

LIBS=zmq

CFLAGS=-O0 -Wall -std=c99 -pedantic
LFLAGS=-l$(LIBS)

.PHONY:	clean

all:	client server

%.o:	%.c
	$(CC) -c -o $@ $(CFLAGS) $<

client:	client.o
	$(CC) -o $@ $(LFLAGS) $<

server:	server.o
	$(CC) -o $@ $(LFLAGS) $<

clean:
	rm -f client.o \
	rm -f server.o \
	rm -f client \
	rm -f server
