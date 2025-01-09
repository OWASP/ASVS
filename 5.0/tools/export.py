#!/usr/bin/python

''' Tool for converting the ASVS requirements to various formats.

    Usage: ./export.py [--format <csv/xml/json]

    By Bernhard Mueller

    Copyright (c) 2017 OWASP Foundation

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

    '''

import argparse
from asvs import ASVS
from cyclonedx import CycloneDX

parser = argparse.ArgumentParser(description='Export the ASVS requirements.')
parser.add_argument('--format', choices=['json', 'json_flat', 'xml', 'csv', 'cdx_json', 'raw', 'json_xl', 'v4_mapping', 'v5_mapping'], default='json')
parser.add_argument('--language', default='en')
parser.add_argument('--verify-only', action='store_true')
parser.add_argument('--raw-folder', default='')
#parser.add_argument('--verify-only', default=False)

args = parser.parse_args()

m = ASVS(args.language)

if bool(args.verify_only):
    if args.format == "csv":
        print(m.verify_csv(m.to_csv()))
    elif args.format == "xml":
        print(m.verify_xml(m.to_xml()))  
    elif args.format == "json_flat":
        print(m.verify_json_flat(m.to_json_flat()))    
    else:
        print(m.verify_json(m.to_json()))    
else:
    if args.format == "csv":
        print(m.to_csv())
    elif args.format == "xml":
        print(m.to_xml())
    elif args.format == "json_flat":
        print(m.to_json_flat())
    elif args.format == "json_xl":
        print(m.to_json_xl())
    elif args.format == "raw":
        print(m.to_raw(args.raw_folder))
    elif args.format == "v4_mapping":
        print(m.to_v4_mapping())
    elif args.format == "v5_mapping":
        print(m.to_v5_mapping())        
    elif args.format == "cdx_json":
        cdx = CycloneDX(m.to_json())
        print(cdx.to_json())
    else:
        print(m.to_json())   