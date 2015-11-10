Sphinx Docker
=============

We have created a 2 Dockerfile's which create docker images for you with all stuff 
in it to build the QGIS-Website or Inasafe- and QGIS-Documentation:

*Dockerfile-html* and docker-build-html.sh together build the images qgis/sphinx_html (417MB) and 
can be used to build html docs and site

*Dockerfile-pdf* and docker-build-pdf.sh together build the images qgis/sphinx_pdf (3.4GB) and 
can be used to build pdf's of the QGIS and Inasafe documentation

The qgis/sphinx_pdf images is based/on top of the qgis/sphinx_html image.

You can also use this Docker images without building by pulling them from hub.docker: https://hub.docker.com/u/qgis/

You will NOT need a python virtual environment for this, because the full 
python environment is in the running container when you run it.

To use:

- have a look into the Dockerfile(s)
- build the image 'qgis/sphinx_html' by running docker-build-html.sh (will take some time)
- build the image 'qgis/sphinx_pdf' by running docker-build-pdf.sh (will take even more time)


Now start a build by either using a full command line like:

     # for example QGIS 2.8 documentation (see README there)
     docker run -v ~/dev/qgis/:/build -w="/build/QGIS-Documentation-2.8" qgis/sphinx_html make html
     # for example Insafe documentation (see README there)
     docker run -t -i -v /home/richard/dev/qgis/git/inasafe-doc:/inasafe-doc -w=/inasafe-doc --rm=true qgis/sphinx_html ./scripts/post_translate.sh en

You can also use these images to build the docs on Windows with boot2docker (tested on Win7 and Win8). Most difficult is the path separator on this operating systems. See https://github.com/AIFDR/inasafe-doc#docker-build-on-your-machine for examples
