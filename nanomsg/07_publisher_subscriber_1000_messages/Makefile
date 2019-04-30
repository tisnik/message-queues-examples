CC=gcc
LINKER=gcc

LIBS=nanomsg

CFLAGS=-O0 -Wall -ansi -pedantic
LFLAGS=-l$(LIBS)

LIBRARY_PATH=/usr/local/lib64/

.PHONY:	clean run_publisher run_subscriber

all:	publisher subscriber

%.o:	%.c
	$(CC) -c -o $@ $(CFLAGS) $<

publisher:	publisher.o
	$(CC) -o $@ $(LFLAGS) $<

subscriber:	subscriber.o
	$(CC) -o $@ $(LFLAGS) $<

clean:
	rm -f publisher.o \
	rm -f subscriber.o \
	rm -f publisher \
	rm -f subscriber

run_publisher:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./publisher

run_subscriber:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./subscriber
