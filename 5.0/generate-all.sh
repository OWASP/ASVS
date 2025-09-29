#!/bin/bash 

ALLOWED_LANGS='en tr'

echo $@

if [[ -n $@ ]]; then
  LANGS=$@
else
  LANGS=${ALLOWED_LANGS}
fi

for lang in ${LANGS}; do
  if [[ " $ALLOWED_LANGS " =~ " $lang " ]]; then

    vers="5.0.0"
    verslong="./docs_$lang/OWASP_Application_Security_Verification_Standard_$vers_$lang"

    python3 tools/export.py --format json --language $lang > "$verslong.json"
    python3 tools/export.py --format cdx_json --language $lang > "$verslong.cdx.json"
    python3 tools/export.py --format json_legacy --language $lang > "$verslong.legacy.json"
    python3 tools/export.py --format json --language $lang --verify-only

    python3 tools/export.py --format json_flat --language $lang > "$verslong.flat.json"
    python3 tools/export.py --format json_flat_legacy --language $lang > "$verslong.flat.legacy.json"
    python3 tools/export.py --format json_flat --language $lang --verify-only

    python3 tools/export.py --format xml --language $lang > "$verslong.xml"
    python3 tools/export.py --format xml_legacy --language $lang > "$verslong.legacy.xml"
    python3 tools/export.py --format xml --language $lang --verify-only

    python3 tools/export.py --format csv --language $lang > "$verslong.csv"
    python3 tools/export.py --format csv_legacy --language $lang > "$verslong.legacy.csv"
    python3 tools/export.py --format csv --language $lang --verify-only

    tools/generate_document.sh $lang $vers

  fi

done
