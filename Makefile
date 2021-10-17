latest: 5.0

all: 5.0 4.0

5.0: docker
	docker run --rm -v "`pwd`/5.0:/data" -v "`pwd`/docker:/scripts" -e "ASVS_VERSION=5.0" asvs/documentbuilder

4.0: docker
	docker run --rm -v "`pwd`/4.0:/data" -v "`pwd`/docker:/scripts" -e "ASVS_VERSION=4.0" asvs/documentbuilder

.PHONY: docker
docker:
	if ! docker image inspect asvs/documentbuilder:latest --format="checking docker image" &> /dev/null; then \
		docker image build --tag asvs/documentbuilder -f docker/Dockerfile docker; \
	fi;
