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
