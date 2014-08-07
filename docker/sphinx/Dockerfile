FROM debian:stable

MAINTAINER Werner Macho <werner.macho@gmail.com>

# Use local cached debs from host (saves your bandwidth!)
# Change ip below to that of your apt-cacher-ng host
# Or comment this line out if you do not with to use caching
#ADD 71-apt-cacher-ng /etc/apt/apt.conf.d/71-apt-cacher-ng

RUN apt-get update
RUN apt-get install -y python2.7 python-pip curl python-setuptools apt-utils
RUN curl https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py | python
RUN curl -o /REQUIREMENTS.txt https://raw.githubusercontent.com/qgis/QGIS-Documentation/master/REQUIREMENTS.txt 
RUN pip install -r /REQUIREMENTS.txt

# to be able to create japanese and russian pdf's you need also:
# for russian pdf you need package 'texinfo texlive-lang-cyrillic' installed
# for japanese pdf you need: 'cmap-adobe-japan1 cmap-adobe-japan2 latex-cjk-all nkf okumura-clsfiles ptex-base ptex-bin texlive-fonts-extra'
RUN apt-get update
RUN apt-get -y -q install texlive-fonts-recommended texinfo texlive-lang-cyrillic 
RUN apt-get -y -q install cmap-adobe-japan1 cmap-adobe-japan2 latex-cjk-all nkf okumura-clsfiles ptex-bin texlive-fonts-extra

# Install Korean packages
RUN apt-get -y -q install ko.tex-base ko.tex-extra fonts-nanum fonts-nanum-extra fonts-nanum-coding fonts-nanum-eco fonts-nanum-gothic-light fonts-unfonts-core

# Install Hindi packages
RUN apt-get -y -q install texlive-lang-indic latex-sanskrit fonts-lohit-deva fonts-deva-extra fonts-nakula fonts-sahadeva fonts-samyak-deva




