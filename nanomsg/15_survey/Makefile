CC=gcc
LINKER=gcc

LIBS=nanomsg

CFLAGS=-O0 -Wall -pedantic
LFLAGS=-l$(LIBS)

LIBRARY_PATH=/usr/local/lib64/

.PHONY:	clean run_client run_server

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

run_client:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./client

run_server:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./server
