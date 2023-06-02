#!/bin/bash 

ALLOWED_LANGS='ar de en es fr pt ru zh-cn'

if [[ -n $@ ]]; then
  LANGS=$@
else
  LANGS='en'
fi

for lang in ${LANGS}; do
  if [[ " $ALLOWED_LANGS " =~ " $lang " ]]; then

    vers="4.0.3"
    verslong="./docs_$lang/OWASP Application Security Verification Standard $vers-$lang"

    python3 tools/export.py --format json --language $lang > "$verslong.json"
    python3 tools/export.py --format json --language $lang --verify-only true

    python3 tools/export.py --format json_flat --language $lang > "$verslong.flat.json"
    python3 tools/export.py --format json_flat --language $lang --verify-only true

    python3 tools/export.py --format xml --language $lang > "$verslong.xml"
    python3 tools/export.py --format xml --language $lang --verify-only true

    python3 tools/export.py --format csv --language $lang > "$verslong.csv"
    python3 tools/export.py --format csv --language $lang --verify-only true

    ./generate_document.sh $lang $vers

  fi

done
