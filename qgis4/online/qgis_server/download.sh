#! /bin/bash

URL=http://37.187.164.233/qgis-server-perfsuite/

mkdir -p data

cd data && wget --reject="index.html*" --no-parent -nH -r --cut-dirs=1 $URL/
