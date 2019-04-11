#! /bin/bash

# download data
if [ ! -d "$ROOT/data" ]
then
	sh download.sh
fi

# stop and restart
docker-compose down
docker-compose rm -f
docker-compose up -d
