#! /bin/bash

. ~/.py-env/bin/activate

case $TARGET in
  4.0)
    ./generate-all.sh $LANGS
    ;;
  5.0)
    if [ -n "$LANGS" ]; then
      export SELECTED_LANGS="$LANGS"
    fi
    make $FORMATS
    ;;
  clean)
    make clean
    ;;
  *)
    make $FORMATS
    ;;
esac
