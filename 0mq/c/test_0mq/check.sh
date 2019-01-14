gcc -c -Wall -ansi -pedantic -o test_0mq.o test_0mq.c
gcc -o test_0mq -lzmq test_0mq.o
