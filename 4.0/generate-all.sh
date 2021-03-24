#!/bin/bash

lang="en"
vers="4.0"
verslong="./docs_$lang/OWASP Application Security Verification Standard $vers-$lang"

python3 export.py --format json --language $lang >"$verslong.json"
python3 export.py --format json_flat --language $lang >"$verslong.flat.json"
python3 export.py --format xml --language $lang >"$verslong.xml"
python3 export.py --format csv --language $lang >"$verslong.csv"
python3 export.py --format oc --language $lang >"$verslong.opencontrol.yaml"

./generate_document.sh $lang $vers
