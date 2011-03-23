# hortont.com build system

.IGNORE:
.SILENT:

baseurl=$(shell PYTHONPATH=build python -c 'import settings; print settings.www_prefix')

all: clean unclean copy-data build-parallel
	python ./build/stats.py

clean:
	rm -rf output

unclean:
	mkdir output

build-parallel:
	sh ./build/parallelBuild.sh

all-serial: clean unclean copy-data
	python ./build/buildPosts.py
	python ./build/buildStatic.py
	python ./build/buildArchive.py
	python ./build/buildRSS.py
	python ./build/buildEverything.py

	python ./build/stats.py

new-post:
	python ./build/newPost.py

copy-data:
	cp -r images output/images
	cp -r styles output/styles

	python ./build/substituteSettings.py output/styles
	python ./build/cssmin.py output/styles

check-links:
	python ./build/testLinks.py

push:
	rm -rf /tmp/hortont.com
	cd /tmp ; git clone git@github.com:hortont424/hortont.com
	cd /tmp/hortont.com ; make ; rsync -a --progress /tmp/hortont.com/output/ hortont.com:/srv/www

.PHONY: all clean copy-data push all-serial
