#! /bin/bash

case $TARGET in
  4.0)
    ./generate-all.sh $LANGS
    ;;
  clean)
    make clean
    ;;
  *)
    make $FORMATS
    ;;
esac
