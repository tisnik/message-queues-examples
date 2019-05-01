CC=gcc
LINKER=gcc

LIBS=nanomsg

CFLAGS=-O0 -Wall -pedantic
LFLAGS=-l$(LIBS)

LIBRARY_PATH=/usr/local/lib64/

.PHONY:	clean run_publisher run_subscriber

all:	publisher subscriber_all subscriber_0 subscriber_1

%.o:	%.c
	$(CC) -c -o $@ $(CFLAGS) $<

publisher:	publisher.o
	$(CC) -o $@ $(LFLAGS) $<

subscriber_0:	subscriber_0.o
	$(CC) -o $@ $(LFLAGS) $<

subscriber_1:	subscriber_1.o
	$(CC) -o $@ $(LFLAGS) $<

subscriber_all:	subscriber_all.o
	$(CC) -o $@ $(LFLAGS) $<

clean:
	rm -f *.o \
	rm -f publisher \
	rm -f subscriber_0 \
	rm -f subscriber_1 \
	rm -f subscriber_all

run_publisher:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./publisher

run_subscriber_0:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./subscriber_0

run_subscriber_1:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./subscriber_1

run_subscriber_all:
	LD_LIBRARY_PATH=$(LIBRARY_PATH) ./subscriber_all
