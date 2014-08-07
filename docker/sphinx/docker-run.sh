# to be able to run the full image (including pulling from transifex)
# you need a valid .transifexrc file with your credentials in your home dir
# this one is temporarily copied to the project dir
# and removed after build
# maybe better to create a qgisdocker transifex user?

cd /home/richard/dev/qgis/git/QGIS-Documentation-2.2/
cp /home/richard/.transifexrc .
docker run -v /home/richard/dev/qgis/git/:/git/doc -w="/git/doc/QGIS-Documentation-2.0" qgis/sphinx:2 make $@
rm -rf .transifexrc
