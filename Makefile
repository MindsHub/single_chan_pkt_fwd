# single_chan_pkt_fwd
# Single Channel LoRaWAN Gateway

CC=g++
CFLAGS=-c -Wall
LIBS=-lwiringPi

all: single_chan_pkt_fwd

single_chan_pkt_fwd: main.o
	$(CC) main.o $(LIBS) -o single_chan_pkt_fwd

main.o: main.cpp
	$(CC) $(CFLAGS) main.cpp

clean:
	rm *.o single_chan_pkt_fwd	