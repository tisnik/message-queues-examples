CC=gcc
LINKER=gcc

LIBS=nanomsg

CFLAGS=-O0 -Wall -ansi -pedantic
LFLAGS=-l$(LIBS)

LIBRARY_PATH=/usr/local/lib64/

.PHONY:	clean run_sender run_receiver

all:	sender receiver

%.o:	%.c
	$(CC) -c -o $@ $(CFLAGS) $<

sender:	sender.o
	$(CC) -o $@ $(LFLAGS) $<

receiver:	receiver.o
	$(CC) -o $@ $(LFLAGS) $<

clean:
	rm -f sender.o \
	rm -f receiver.o \
	rm -f sender \
	rm -f receiver

run_sender:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./sender

run_receiver:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./receiver
