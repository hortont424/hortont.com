# hortont.com build system

.IGNORE:
.SILENT:

baseurl=$(shell PYTHONPATH=build python2.6 -c 'import settings; print settings.www_prefix')

all: clean unclean copy-data build-parallel
	python2.6 ./build/stats.py

clean:
	rm -rf output

unclean:
	mkdir output

build-parallel:
	./build/parallelBuild.sh

all-serial: clean unclean copy-data
	python2.6 ./build/buildPosts.py
	python2.6 ./build/buildStatic.py
	python2.6 ./build/buildArchive.py
	python2.6 ./build/buildRSS.py
	python2.6 ./build/buildEverything.py

	python2.6 ./build/stats.py

new-post:
	python2.6 ./build/newPost.py

copy-data:
	cp -r images output/images
	cp -r styles output/styles

	python2.6 ./build/substituteSettings.py output/styles
	python2.6 ./build/cssmin.py output/styles

check-links:
	python2.6 ./build/testLinks.py

push:
	rm -rf /tmp/hortont.com
	cd /tmp ; git clone git@github.com:hortont424/hortont.com
	cd /tmp/hortont.com ; make ; rsync -a --progress /tmp/hortont.com/output/ hortont.com:/srv/www

.PHONY: all clean copy-data push all-serial
