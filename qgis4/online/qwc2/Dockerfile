FROM debian:stable
RUN  export DEBIAN_FRONTEND=noninteractive
ENV  DEBIAN_FRONTEND noninteractive

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y curl gnupg git apt-transport-https

RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list
RUN curl -sL https://deb.nodesource.com/setup_9.x | bash -
RUN apt-get update \
    && apt-get install -y yarn nodejs

WORKDIR /root
RUN git clone --recursive https://github.com/qgis/qwc2-demo-app.git

WORKDIR /root/qwc2-demo-app
COPY config.json config.json
RUN yarn install
RUN yarn run prod
RUN tar zcvf prod.tar.gz prod
