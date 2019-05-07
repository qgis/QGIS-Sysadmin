#! /bin/bash

if [ ! -d "./graffiti" ]
then
  git clone https://github.com/pblottiere/graffiti
  cd graffiti
  mkdir venv
  virtualenv -p /usr/bin/python3 ./venv
  . venv/bin/activate
  pip install -r requirements.txt
  deactivate
  cd -
fi

rm -rf /tmp/graffiti_aggregate/
. graffiti/venv/bin/activate
python aggregate.py

scp /tmp/graffiti_aggregate/aggregate.html qgis-test:/var/www/qgisdata/QGIS-tests/perf_test/graffiti/aggregate/
scp /tmp/graffiti_aggregate/style.css qgis-test:/var/www/qgisdata/QGIS-tests/perf_test/graffiti/aggregate/
scp qgis.png qgis-test:/var/www/qgisdata/QGIS-tests/perf_test/graffiti/aggregate/logo.png
scp -r /tmp/graffiti_aggregate/graph qgis-test:/var/www/qgisdata/QGIS-tests/perf_test/graffiti/aggregate/
