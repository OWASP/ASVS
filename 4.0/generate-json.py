#!/usr/bin/env python

''' ASVS document parser and converter class.
    Based upon code written for MASVS By Bernhard Mueller
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

import os
import re
import json
import argparse

class ASVS:
    ''' Creates json representation of the ASVS from markdown files.
    
        On Windows 10, can be run as:
        python .\generate-json.py --file "OWASP Application Security Verification Standard 4.0-en.json" --encoding UTF-8
        
        On Linux (tested on Kali), can be run as:
        python3 ./generate-json.py --file "OWASP Application Security Verification Standard 4.0-en.json" --encoding UTF-8
    '''
    
    asvs = {}
    asvs['Name'] = "Application Security Verification Standard Project"
    asvs['ShortName'] = "ASVS"
    asvs['Version'] = ""
    asvs['Description'] = "The OWASP Application Security Verification Standard (ASVS) Project provides a basis for testing web application technical security controls and also provides developers with a list of requirements for secure development."

    regex = re.compile('Version (([\d.]+){3})')

    for line in open(os.path.join("en", "0x01-Frontispiece.md"), encoding="utf8"):
        m = re.search(regex, line)
        if m:
            asvs['Version'] = m.group(1)
            break
    
    regex = re.compile('## About the Standard\n\n(.*)')

    with open(os.path.join("en", "0x01-Frontispiece.md"), encoding="utf8") as content:
        m = re.search(regex, content.read())
        if m:
            asvs['Description'] = m.group(1)
    
    asvs['Requirements'] = chapters = []

    def __init__(self):
        for file in os.listdir("en"):

            if re.match("0x\d{2}-V", file):
                chapter = {};
                chapter['Shortcode'] = ""
                chapter['Ordinal'] = ""
                chapter['ShortName'] = ""
                chapter['Name'] = ""
                chapter['Items'] = []

                section = {}
                section['Shortcode'] = ""
                section['Ordinal'] = ""
                section['Name'] = ""
                section['Items'] = []

                regex = re.compile('0x\d{2}-(V([0-9]{1,3}))-(\w[^-.]*)')
                m = re.search(regex, file)
                if m:
                    chapter = {};
                    chapter['Shortcode'] = m.group(1)
                    chapter['Ordinal'] = int(m.group(2))
                    chapter['ShortName'] = m.group(3)
                    chapter['Name'] = ""
                    chapter['Items'] = []

                    section = {}
                    section['Shortcode'] = m.group(1)
                    section['Ordinal'] = int(m.group(2))
                    section['Name'] = m.group(3)
                    section['Items'] = []
                    
                    self.chapters.append(chapter)

                for line in open(os.path.join("en", file), encoding="utf8"):
                    regex = re.compile('# (V([0-9]{1,2})): ([\w\s][^\n]*)')
                    m = re.search(regex, line)
                    if m:
                        chapter['Name'] = m.group(3)


                    regex = re.compile('## (V[0-9]{1,2}.([0-9]{1,3})) ([\w\s][^\n]*)')
                    m = re.search(regex, line)
                    if m:
                        section = {}
                        section['Shortcode'] = m.group(1)
                        section['Ordinal'] = int(m.group(2))
                        section['Name'] = m.group(3)
                        section['Items'] = []

                        chapter['Items'].append(section)

                    regex = re.compile('\*\*([\d\.]+)\*\*\s\|\s{0,1}(.*?)\s{0,1}\|([\w\d,\. ✓]*)\|([\w\d,\. ✓]*)\|([\w\d,\. ✓]*)\|([0-9,\s]*)\|([A-Z0-9/\s,.]*)\|{0,1}')
                    m = re.search(regex, line)
                    if m:
                        req = {}
                        req['Shortcode'] = "V" + m.group(1)
                        req['Ordinal'] = int(m.group(1).rsplit('.', 1)[1])
                        req['Description'] = m.group(2)

                        level1 = {}
                        level2 = {}
                        level3 = {}

                        level1['Required'] = m.group(3).strip() != ''
                        level2['Required'] = m.group(4).strip() != ''
                        level3['Required'] = m.group(5).strip() != ''

                        level1['Requirement'] = ("Optional" if m.group(3).strip('✓ ') == "o" else m.group(3).strip('✓ '))
                        level2['Requirement'] = ("Optional" if m.group(4).strip('✓ ') == "o" else m.group(4).strip('✓ '))
                        level3['Requirement'] = ("Optional" if m.group(5).strip('✓ ') == "o" else m.group(5).strip('✓ '))

                        req['L1'] = level1
                        req['L2'] = level2
                        req['L3'] = level3

                        req['CWE'] = [int(i.strip()) for i in filter(None, m.group(6).strip().split(','))]
                        req['NIST'] = [str(i.strip()) for i in filter(None,m.group(7).strip().split('/'))]

                        section['Items'].append(req)

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.asvs, indent = 2, sort_keys = False).strip()

m = ASVS()

parser = argparse.ArgumentParser(description='Export the ASVS to structured JSON.')
parser.add_argument('--file', required = False)
parser.add_argument('--encoding', choices=['UTF-16', 'UTF-8'], default = 'UTF-8', required = False)
args = parser.parse_args()

if args.file == None:
    print(m.to_json())
else:
    stream = open(args.file, 'w', encoding = args.encoding, closefd = True)
    stream.write(m.to_json())
    stream.close()
