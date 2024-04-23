#!/bin/bash 

ALLOWED_LANGS='en'

echo $@

if [[ -n $@ ]]; then
  LANGS=$@
else
  LANGS=${ALLOWED_LANGS}
fi

for lang in ${LANGS}; do
  if [[ " $ALLOWED_LANGS " =~ " $lang " ]]; then

    vers="5.0"
    verslong="./docs_$lang/OWASP Application Security Verification Standard $vers-$lang"

    python3 tools/export.py --format json --language $lang > "$verslong.json"
    python3 tools/export.py --format cdx_json --language $lang > "$verslong.cdx.json"
    python3 tools/export.py --format reqw_json --language $lang > "$verslong.reqw"
    python3 tools/export.py --format json --language $lang --verify-only true

    python3 tools/export.py --format json_flat --language $lang > "$verslong.flat.json"
    python3 tools/export.py --format json_flat --language $lang --verify-only true

    python3 tools/export.py --format xml --language $lang > "$verslong.xml"
    python3 tools/export.py --format xml --language $lang --verify-only true

    python3 tools/export.py --format csv --language $lang > "$verslong.csv"
    python3 tools/export.py --format csv --language $lang --verify-only true

    tools/generate_document.sh $lang $vers

  fi

done
