FROM debian:stable

MAINTAINER Werner Macho <werner.macho@gmail.com>

RUN apt-get update
RUN apt-get install -y python2.7 python-pip curl python-setuptools apt-utils
RUN curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python
RUN curl -o /REQUIREMENTS.txt https://raw.githubusercontent.com/qgis/QGIS-Documentation/master/REQUIREMENTS.txt 
RUN pip install -r /REQUIREMENTS.txt

# to be able to create japanese and russian pdf's you need also:
# for russian pdf you need package 'texinfo texlive-lang-cyrillic' installed
# for japanese pdf you need: 'cmap-adobe-japan1 cmap-adobe-japan2 latex-cjk-all nkf okumura-clsfiles ptex-base ptex-bin texlive-fonts-extra'
RUN apt-get install -y texlive-fonts-recommended texinfo texlive-lang-cyrillic cmap-adobe-japan1 cmap-adobe-japan2 latex-cjk-all nkf okumura-clsfiles ptex-bin texlive-fonts-extra


