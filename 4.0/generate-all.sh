#!/bin/bash 

lang="en"
vers="4.0.2"
verslong="./docs_$lang/OWASP Application Security Verification Standard $vers-$lang"

python3 export.py --format json --language $lang > "$verslong.json"
python3 export.py --format json_sant --language $lang > "$verslong.sant.json"
python3 export.py --format xml --language $lang > "$verslong.xml"
python3 export.py --format csv --language $lang > "$verslong.csv"

./generate_document.sh $lang $vers
