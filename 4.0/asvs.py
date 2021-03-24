#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' ASVS document parser and converter class.

    Based upon code written for MASVS By Bernhard Mueller
    Significant improvement by Jonny Schnittger @JonnySchnittger
    Additional modifications by Josh Grossman @tghosth
    Copyright (c) 2020 OWASP Foundation

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
import yaml
from xml.sax.saxutils import escape
import csv
import dicttoxml

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class ASVS:
    asvs = {}
    asvs['Name'] = "Application Security Verification Standard Project"
    asvs['ShortName'] = "ASVS"
    asvs['Version'] = ""
    asvs['Description'] = "The OWASP Application Security Verification Standard (ASVS) Project " \
        "provides a basis for testing web application technical security controls and also " \
        "provides developers with a list of requirements for secure development."

    asvs_flat = []
    asvs_flat2 = {}
    asvs_flat2['requirements'] = []
    asvs_opencontrol = {}

    def __init__(self, language):

        regex = re.compile('Version (([\d.x]+){3})')

        for line in open(os.path.join(language, "0x01-Frontispiece.md"), encoding="utf8"):
            m = re.search(regex, line)
            if m:
                self.asvs['Version'] = m.group(1)
                break

        regex = re.compile('## About the Standard\n\n(.*)')

        with open(os.path.join(language, "0x01-Frontispiece.md"), encoding="utf8") as content:
            m = re.search(regex, content.read())
            if m:
                self.asvs['Description'] = m.group(1)

        self.asvs['Requirements'] = chapters = []


        for file in os.listdir(language):

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

                    chapters.append(chapter)

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

                    regex = re.compile("\*\*([\d\.]+)\*\*\s\|\s{0,1}(.*?)\s{0,1}\|([\w\d,\. ✓]*)"\
                        "\|([\w\d,\. ✓]*)\|([\w\d,\. ✓]*)\|([0-9,\s]*)\|([A-Z0-9/\s,.]*)\|{0,1}")
                    m = re.search(regex, line)
                    if m:

                        opencontrol_flat = {}
                        opencontrol_flat['family'] = f"{chapter['ShortName']}-{section['Ordinal']}"
                        req_flat = {}
                        req_flat2 = {}
                        req_flat2['Section'] = req_flat['chapter_id'] = chapter['Shortcode']
                        req_flat2['Name'] = req_flat['chapter_name'] = chapter['Name']
                        req_flat['section_id'] = section['Shortcode']
                        req_flat['section_name'] = opencontrol_flat['name'] = section['Name']

                        req = {}
                        req_flat2['Item'] = req_flat['req_id'] = req['Shortcode'] = "V" + m.group(1)
                        req['Ordinal'] = int(m.group(1).rsplit('.', 1)[1])
                        req_flat2['Description'] = req_flat['req_description'] = req['Description'] = opencontrol_flat['description'] = m.group(2)

                        level1 = {}
                        level2 = {}
                        level3 = {}

                        req_flat['level1'] = m.group(3).strip(' ')
                        req_flat['level2'] = m.group(4).strip(' ')
                        req_flat['level3'] = m.group(5).strip(' ')

                        level1['Required'] = m.group(3).strip() != ''
                        req_flat2['L1'] = ('X' if level1['Required'] else '')
                        level2['Required'] = m.group(4).strip() != ''
                        req_flat2['L2'] = ('X' if level2['Required'] else '')
                        level3['Required'] = m.group(5).strip() != ''
                        req_flat2['L3'] = ('X' if level3['Required'] else '')

                        level1['Requirement'] = ("Optional" if m.group(3).strip('✓ ') == "o" else m.group(3).strip('✓ '))
                        level2['Requirement'] = ("Optional" if m.group(4).strip('✓ ') == "o" else m.group(4).strip('✓ '))
                        level3['Requirement'] = ("Optional" if m.group(5).strip('✓ ') == "o" else m.group(5).strip('✓ '))

                        req['L1'] = level1
                        req['L2'] = level2
                        req['L3'] = level3

                        req['CWE'] = [int(i.strip()) for i in filter(None, m.group(6).strip().split(','))]
                        req_flat2['CWE'] = req_flat['cwe'] = m.group(6).strip()
                        req['NIST'] = [str(i.strip()) for i in filter(None,m.group(7).strip().split('/'))]
                        req_flat2['NIST'] = req_flat['nist'] = m.group(7).strip()

                        section['Items'].append(req)
                        self.asvs_flat.append(req_flat)
                        self.asvs_flat2['requirements'].append(req_flat2)
                        self.asvs_opencontrol[req['Shortcode']]=opencontrol_flat

    def sorted_nicely(self, l ):
        """ Sort the given iterable in the way that humans expect."""
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
        return sorted(l, key = alphanum_key)

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.asvs, indent = 2, sort_keys = False).strip()

    def to_json_flat(self):
        ''' Returns a JSON-formatted string which is flattened and simpler '''
        return json.dumps(self.asvs_flat2, indent = 2, sort_keys = False).strip()

    def to_xmlOLD(self):
        ''' Returns XML '''
        xml = ''

        for r in self.requirements:

            xml += "<requirement id = \"" + escape(r['id']) + "\">" + escape(r['text']) + "</requirement>\n"

        return xml
    def to_xml(self):
        return dicttoxml.dicttoxml(self.asvs, attr_type=False).decode('utf-8')

    def to_csv(self):
        ''' Returns CSV '''
        si = StringIO()

        writer = csv.DictWriter(si, ['chapter_id', 'chapter_name', 'section_id', 'section_name', 'req_id', 'req_description', 'level1', 'level2', 'level3', 'cwe', 'nist'])
        writer.writeheader()
        writer.writerows(self.asvs_flat)

        return si.getvalue()

    def to_opencontrol(self):
        ''' Returns opencontrol yaml '''

        opencontrol_result=yaml.dump({'name':f"{self.asvs['ShortName']}-{self.asvs['Version']}"})
        for key in self.sorted_nicely(self.asvs_opencontrol.keys()):
            opencontrol_result+=yaml.dump({
                key:{
                    "family":self.asvs_opencontrol[key]["family"],
                    "name":self.asvs_opencontrol[key]["name"],
                    "description":self.asvs_opencontrol[key]["description"]
                }
            },sort_keys=False)

        return opencontrol_result
