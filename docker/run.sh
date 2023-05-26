#! /bin/bash

case $TARGET in
  4.0)
    ./generate-all.sh
    ;;
  clean)
    make clean
    ;;
  *)
    make $FORMATS
    ;;
esac
