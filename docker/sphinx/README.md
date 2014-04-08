Sphinx Docker
=============

We have created a Dockerfile which creates a docker image for you with all stuff 
in it to build the Website or Documentation.

You will NOT need a python virtual environment for this, because the full 
python environment is in the running container.

To use:

- have a look into the Dockerfile, comment the last line if you do NOT want to build pdf's in non western charactersets. For testing it is also easier to comment this line, because it makes your image 1Gb larger...
- build the image 'qgis/sphinx:1.0' by running docker-build.sh (will take some time)
- now start a build by either using a full commanline like:

    docker run -v ~/dev/qgis/:/build -w="/build/QGIS-Documentation-2.0" qgis/sphinx make html

- or just run the docker-run.sh 

I had issues with the tx-client on windows, so remove the tx-steps from the Makefile for testing


Scripts:


    docker-build.sh     builds a docker image with all stuff in it to build 
                        all docks (including all fonts and latex/pdf related stuff)

    docker-run.sh       script to run it


Run:

    # clone/checkout a for example QGIS-Documentation in ~/dev/qgis
    # now from ~/dev/qgis run docker-run.sh
    # or from command line like: 
    docker run -v ~/dev/qgis/:/build -w="/build/QGIS-Documentation-2.0" qgis/sphinx make html


