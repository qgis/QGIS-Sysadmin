#! /bin/bash

# stop all containers
docker stop $(docker ps -a -q)

# remove all containers
docker rm $(docker ps -a -q)

# remove docker images depending on debian testing
docker rmi qgisserver-perfsuite/3.10
docker rmi qgisserver-perfsuite/3.14
docker rmi qgisserver-perfsuite/master

docker rmi qgisserver-certifsuite/3.4
docker rmi qgisserver-certifsuite/master

docker rmi debian:testing
docker rmi debian:sid

# remove static qwc2 file
rm -rf /home/{{ user }}/demos/qwc2/demos_qwc2
