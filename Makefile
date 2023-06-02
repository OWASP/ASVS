latest: 5.0

all: 5.0 4.0

4.0-LANGS := $(shell cd 4.0 && git status --porcelain | sed 's/[ A-Z?]\+ \"\?4.0\///g' | sed 's/\/.*//g' | sed -n '/^\(ar\|de\|en\|es\|fr\|pt\|ru\|zh-cn\)/p' | tr '\n' ' ')

5.0: docker
	docker run --rm -v "`pwd`/5.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=5.0" -e "FORMATS=$(FORMATS)" asvs/documentbuilder
5.0-clean: docker
	docker run --rm -v "`pwd`/5.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=clean" -e "FORMATS=$(FORMATS)" asvs/documentbuilder

4.0: docker
	docker run --rm -v "`pwd`/4.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=4.0" -e "FORMATS=$(FORMATS)" -e "LANGS=$(4.0-LANGS)" asvs/documentbuilder
4.0-clean: docker
	docker run --rm -v "`pwd`/4.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=clean" -e "FORMATS=$(FORMATS)" asvs/documentbuilder

.PHONY: docker
docker:
	if ! docker image inspect asvs/documentbuilder:latest --format="checking docker image" &> /dev/null; then \
		docker build --build-arg CERT_FILE=docker/cert --tag asvs/documentbuilder:latest --network host docker; \
	fi;
