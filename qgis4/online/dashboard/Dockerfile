FROM debian:stable
RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y ruby2.3-dev gcc make g++ nodejs

WORKDIR /root
COPY site.tar.gz site.tar.gz
RUN tar zxf site.tar.gz

WORKDIR /root/site
RUN gem install dashing
RUN gem install bundler
RUN bundle

CMD ["dashing", "start"]
