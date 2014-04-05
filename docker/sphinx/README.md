Sphinx Docker
=============

Scripts::


    docker-build.sh     builds a docker image with all stuff in it to build 
                        all docks (including all fonts and latex/pdf related stuff)

    docker-run.sh       script to run it


Use::

    # clone/checkout a for example QGIS-Documentation in ~/dev/qgis
    # now from ~/dev/qgis run docker-run.sh
    # or from command line like: 
    docker run -v ~/dev/qgis/:/build -w="/build/QGIS-Documentation-2.0" qgis/sphinx make html


