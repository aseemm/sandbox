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

# set up the google test framework
RUN apt-get install -y libgtest-dev
RUN apt-get install -y cmake
RUN cd /usr/src/gtest; cmake CMakeLists.txt; make; cp *.a /usr/lib

# RUN git clone -q https://github.com/google/googletest.git /googletest \
#  && mkdir -p /googletest/build \
#  && cd /googletest/build \
#  && cmake .. && make && make install \
#  && cd / && rm -rf /googletest

# ARG BRANCH_OR_TAG=master
# ARG CMAKE_OPTIONS=-std=c++11
# ENV DEBIAN_FRONTEND=noninteractive
# RUN env \
#   && apt-get update \
#   && apt-get install -q -y git cmake make g++ lcov \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*
# 
# RUN git clone --depth=1 -b $BRANCH_OR_TAG -q https://github.com/google/googletest.git /googletest
# RUN mkdir -p /googletest/build
# WORKDIR /googletest/build
# RUN cmake .. ${CMAKE_OPTIONS} && make && make install
# RUN mkdir -p /code
# WORKDIR /code
# RUN rm -rf /googletest

# copy over source code
COPY src /src
WORKDIR /src

# RUN g++ -o hello_world hello_world.c
# CMD ["./hello_world"]

# RUN g++ -o pointers pointers.c
# CMD ["./pointers"]

# RUN g++ -o linkedlists linkedlists.c
# CMD ["./linkedlists"]

# RUN g++ -o hashmap hashmap.c
# CMD ["./hashmap"]

# RUN g++ -o whattotest whattotest.cpp
# CMD ["./whattotest"]

RUN g++ -Wall -Werror -Wextra -pedantic -O0 -std=c++11 -o tests bitmanip_unittest.cpp /usr/lib/libgtest.a -lpthread
CMD ["./tests"]