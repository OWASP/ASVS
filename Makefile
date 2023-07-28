latest: 5.0

all: 5.0 4.0

4.0-LANGS := $(shell cd 4.0 && git status --porcelain | sed 's/[ A-Z?]\+ \"\?4.0\///g' | sed 's/\/.*//g' | sed -n '/^\(ar\|de\|en\|es\|fr\|pt\|ru\|zh-cn\)/p' | tr '\n' ' ')

5.0:
	docker run --rm --user $(id -u):$(id -g) -v "`pwd`/5.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=5.0" -e "FORMATS=$(FORMATS)" ghcr.io/asvs/documentbuilder
5.0-clean:
	docker run --rm --user $(id -u):$(id -g) -v "`pwd`/5.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=clean" -e "FORMATS=$(FORMATS)" ghcr.io/asvs/documentbuilder

4.0:
	docker run --rm --user $(id -u):$(id -g) -v "`pwd`/4.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=4.0" -e "FORMATS=$(FORMATS)" -e "LANGS=$(4.0-LANGS)" ghcr.io/asvs/documentbuilder
4.0-clean:
	docker run --rm --user $(id -u):$(id -g) -v "`pwd`/4.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=clean" -e "FORMATS=$(FORMATS)" ghcr.io/asvs/documentbuilder

.PHONY: 5.0 5.0-clean 4.0 4.0-clean docker
docker:
	docker build --build-arg CERT_FILE=docker/cert --tag ghcr.io/asvs/documentbuilder:latest --network host docker
