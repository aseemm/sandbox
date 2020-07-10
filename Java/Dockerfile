FROM alpine:3.6
 
MAINTAINER java-success.com
 
# working directory in the container where Helloworld.java & run.sh copied to 
WORKDIR /src
 
# run as a container root user 
USER root
 
# install required packages
RUN apk add --no-cache openssh openssl openjdk8 rsync bash procps nss
 
# set JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk
ENV PATH $PATH:$JAVA_HOME/bin
 
# copy into the container working folder
COPY src /src

RUN javac Helloworld.java
 
# execute the run.sh bash file
CMD ["java", "Helloworld"]
