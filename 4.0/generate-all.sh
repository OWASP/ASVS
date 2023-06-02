#!/bin/bash 

LANGS="${@:=en}"

for lang in ${LANGS}; do

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

done
