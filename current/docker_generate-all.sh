#! /bin/bash

docker build -t asvs-builder .

docker run -it -v ${PWD}:/app -w /app --entrypoint /app/generate-all.sh asvs-builder 