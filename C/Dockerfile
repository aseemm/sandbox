# Select build node OS
FROM ubuntu:16.04

# Update apt-get
RUN apt-get update

# Install gcc and g++
RUN apt-get install -y gcc
RUN apt-get install -y g++
RUN apt-get install -y make
RUN apt-get install -y gdb
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN apt-get install -y file
RUN apt-get install -y git
RUN apt-get install -y man
RUN apt-get install -y libc6-dev-i386
RUN apt-get install -y netcat

# copy over source code
COPY src /src
WORKDIR /src

# RUN g++ -o hello_world hello_world.c
# CMD ["./hello_world"]

RUN g++ -o pointers pointers.c
CMD ["./pointers"]