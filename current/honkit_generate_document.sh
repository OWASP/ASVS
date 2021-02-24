#! /bin/bash
set -e 

function honkit(){
    docker run -v $repo_root:$repo_root -w /$repo_root/current/$lang --rm -it honkit/honkit honkit $@
}

docker --version > /dev/null
repo_root=$(git rev-parse --show-toplevel)
cwd=$(pwd)
lang=$1
format=$2
output=$3

mkdir -p $repo_root/out
honkit $format ./ /$repo_root/out/$output
