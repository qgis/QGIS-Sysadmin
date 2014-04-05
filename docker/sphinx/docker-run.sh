# to be able to run the full image (including pulling from transifex)
# you need a valid .transifexrc file with your credentials in your home dir
# this one is temporarily copied to the project dir
# and removed after build
# maybe better to create a qgisdocker transifex user?

cd /var/git/QGIS-Documentation-2.0/
cp /home/rduivenvoorde/.transifexrc .
docker run -v /var/git/:/git/doc -w="/git/doc/QGIS-Documentation-2.0" qgis/sphinx:1.0 make $@
rm -rf .transifexrc
