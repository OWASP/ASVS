latest: 5.0

all: 5.0 4.0

4.0-LANGS := $(shell cd 4.0 && git status --porcelain | sed 's/[ A-Z?]\+ \"\?4.0\///g' | sed 's/\/.*//g' | sed -n '/^\(ar\|de\|en\|es\|fr\|pt\|ru\|zh-cn\)/p' | tr '\n' ' ')

5.0: docker
	docker run --rm --user $(id -u):$(id -g) -v "`pwd`/5.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=5.0" -e "FORMATS=$(FORMATS)" ghcr.io/owasp/asvs/documentbuilder:latest
5.0-clean: docker
	docker run --rm --user $(id -u):$(id -g) -v "`pwd`/5.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=clean" -e "FORMATS=$(FORMATS)" ghcr.io/owasp/asvs/documentbuilder:latest

4.0: docker
	docker run --rm --user $(id -u):$(id -g) -v "`pwd`/4.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=4.0" -e "FORMATS=$(FORMATS)" -e "LANGS=$(4.0-LANGS)" ghcr.io/owasp/asvs/documentbuilder:latest
4.0-clean: docker
	docker run --rm --user $(id -u):$(id -g) -v "`pwd`/4.0:/data" -v "`pwd`/docker:/scripts" -e "TARGET=clean" -e "FORMATS=$(FORMATS)" ghcr.io/owasp/asvs/documentbuilder:latest

.PHONY: 5.0 5.0-clean 4.0 4.0-clean docker
docker:
	docker pull ghcr.io/owasp/asvs/documentbuilder:latest || docker build --pull --tag ghcr.io/owasp/asvs/documentbuilder:latest --network host docker
