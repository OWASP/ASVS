#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' ASVS document parser and converter class.

    Based upon code written for MASVS By Bernhard Mueller
    Significant improvement by Jonny Schnittger @JonnySchnittger
    Additional modifications by Josh Grossman @tghosth
    Copyright (c) 2023 OWASP Foundation

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
from xml.sax.saxutils import escape
import csv
from dicttoxml2 import dicttoxml
import xml.etree.ElementTree as ET

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

    asvs_flat = {}
    asvs_flat2 = {}
    asvs_flat['requirements'] = []
    asvs_flat2['requirements'] = []
    language = ''

    def __init__(self, language_in):    
        
        self.language = language_in
        prefix_char1, prefix_char2, prefix_char1_b = self.get_prefix()

        regex = re.compile('Version (([\d.]+){3})')
        
        for line in open(os.path.join(self.language, "0x01-Frontispiece.md"), encoding="utf8"):
            m = re.search(regex, line)
            if m:
                self.asvs['Version'] = m.group(1)
                break

        regex = re.compile('## About the Standard\n\n(.*)')

        with open(os.path.join(self.language, "0x01-Frontispiece.md"), encoding="utf8") as content:
            m = re.search(regex, content.read())
            if m:
                self.asvs['Description'] = m.group(1)

        self.asvs['Requirements'] = chapters = []

    
        for file in sorted(os.listdir(self.language)):

            if re.match("0x\d{2}-V", file):
                chapter = {}
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
                    chapter = {}
                    chapter['Shortcode'] = m.group(1).replace('V', prefix_char1)
                    chapter['Ordinal'] = int(m.group(2))
                    chapter['ShortName'] = m.group(3)
                    chapter['Name'] = ""
                    chapter['Items'] = []

                    section = {}
                    section['Shortcode'] = m.group(1).replace('V', prefix_char1)
                    section['Ordinal'] = int(m.group(2))
                    section['Name'] = m.group(3)
                    section['Items'] = []

                    chapters.append(chapter)

                for line in open(os.path.join(self.language, file), encoding="utf8"):
                    regex = re.compile("^#\s(" + prefix_char1 + "([0-9]{1,2})" + prefix_char1_b + ")\s([\w\s][^\n]*)")
                    
                    #if line.startswith('# '):
                    #    print(line)
                    m = re.search(regex, line)
                    if m:
                        chapter['Name'] = m.group(3)


                    regex = re.compile("## (" + prefix_char2 + "[0-9]{1,2}.([0-9]{1,3})) ([\w\s][^\n]*)")
                    m = re.search(regex, line)
                    if m:
                        section = {}
                        section['Shortcode'] = m.group(1)
                        section['Ordinal'] = int(m.group(2))
                        
                        if self.language == 'ar':
                            section['Ordinal'] = int(m.group(1).split('.')[0].replace(prefix_char2, ''))
                        
                        section['Name'] = m.group(3)
                        section['Items'] = []

                        chapter['Items'].append(section)

                    regex = re.compile("\*\*([\d\.]+)\*\*\s\|\s{0,1}(.*?)\s{0,1}\|(.*?)\|"\
                                        "(.*?)\|(.*?)\|([0-9,\s]*)\|([A-Z0-9/\s,.]*)\|{0,1}")
                    m = re.search(regex, line)
                    if m:
                    
                        req_flat = {}
                        req_flat2 = {}
                        req_flat2['Section'] = req_flat['chapter_id'] = chapter['Shortcode']
                        req_flat2['Name'] = req_flat['chapter_name'] = chapter['Name']
                        req_flat['section_id'] = section['Shortcode']
                        req_flat['section_name'] = section['Name']
                        
                        req = {}
                        req_flat2['Item'] = req_flat['req_id'] = req['Shortcode'] = prefix_char2 + m.group(1)
                        req['Ordinal'] = int(m.group(1).rsplit('.',1)[1])
                        if self.language == 'ar':
                            req['Ordinal'] = int(m.group(1).split('.')[0])

                        req_flat2['Description'] = req_flat['req_description'] = req['Description'] = m.group(2)

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

                        level1['Requirement'] = ("Optional" if m.group(3).strip('✓ ') == "o" else m.group(3).strip(' '))
                        level2['Requirement'] = ("Optional" if m.group(4).strip('✓ ') == "o" else m.group(4).strip(' '))
                        level3['Requirement'] = ("Optional" if m.group(5).strip('✓ ') == "o" else m.group(5).strip(' '))

                        req['L1'] = level1
                        req['L2'] = level2
                        req['L3'] = level3

                        req['CWE'] = [int(i.strip()) for i in filter(None, m.group(6).strip().split(','))]
                        req_flat2['CWE'] = req_flat['cwe'] = m.group(6).strip()
                        req['NIST'] = [str(i.strip()) for i in filter(None,m.group(7).strip().split('/'))]
                        req_flat2['NIST'] = req_flat['nist'] = m.group(7).strip()
                        
                        section['Items'].append(req)
                        self.asvs_flat['requirements'].append(req_flat)
                        self.asvs_flat2['requirements'].append(req_flat2)

    def get_prefix(self):
        prefix_char1 = prefix_char2 = 'V'
        prefix_char1_b = ''
        if self.language == 'ar':
            prefix_char1 = 'ت'
            prefix_char1_b = ':'
            prefix_char2 = 'ق'

        

        return prefix_char1, prefix_char2, prefix_char1_b

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.asvs, indent = 2, sort_keys = False, ensure_ascii=False).strip()

    def to_json_flat(self):
        ''' Returns a JSON-formatted string which is flattened and simpler '''
        return json.dumps(self.asvs_flat, indent = 2, sort_keys = False, ensure_ascii=False).strip()

    def to_xmlOLD(self):
        ''' Returns XML '''
        xml = ''

        for r in self.requirements:

            xml += "<requirement id = \"" + escape(r['id']) + "\">" + escape(r['text']) + "</requirement>\n"

        return xml
    def to_xml(self):
        return dicttoxml(self.asvs, attr_type=False).decode('utf-8')
        
    def to_csv(self):
        ''' Returns CSV '''
        si = StringIO()

        writer = csv.DictWriter(si, ['chapter_id', 'chapter_name', 'section_id', 'section_name', 'req_id', 'req_description', 'level1', 'level2', 'level3', 'cwe', 'nist'])
        writer.writeheader()
        writer.writerows(self.asvs_flat['requirements'])

        return si.getvalue()

    def dict_increment(self, dict_obj, dict_key):
        if dict_key not in dict_obj:
            dict_obj[dict_key] = 0
        
        dict_obj[dict_key] += 1

        return dict_obj
    
    def summary_total(self, summary):
        total = 0
        for chapter in summary:
            total += summary[chapter]
        
        return total

    def summary_string(self, format, summary):
        return f'Language: {self.language}. Format: {format}. Total: {self.summary_total(summary)}. Details: {summary}\n'


    def verify_csv(self, csv):
        
        prefix_char1, null, null = self.get_prefix()

        summary = {}
        for line in csv.splitlines():
            if 'chapter_id,chapter_name' not in line:
                summary = self.dict_increment(summary, line.split(',')[0].replace(prefix_char1,''))

        return self.summary_string('csv', summary)

    def verify_json_flat(self, json_flat):
        prefix_char1, null, null = self.get_prefix()
        data = json.loads(json_flat)
        summary = {}
        for req in data['requirements']:
            summary = self.dict_increment(summary, req['chapter_id'].replace(prefix_char1,''))

        return self.summary_string('json_flat', summary)

    def verify_json(self, json_reg):
        prefix_char1, null, null = self.get_prefix()
        data = json.loads(json_reg)
        summary = {}
        for req in data['Requirements']:
            for ite1 in req['Items']:
                for ite2 in ite1['Items']:
                    summary = self.dict_increment(summary, req['Shortcode'].replace(prefix_char1,''))

        return self.summary_string('json', summary)


    def verify_xml(self, xml_string):
        prefix_char1, null, null = self.get_prefix()
        data = ET.fromstring(xml_string)
        summary = {}
        scode = ''
        for req in data.iter():
            if req.tag == 'Requirements':
                for el_item in req:
                    for el_item_sub in el_item:
                        if el_item_sub.tag == 'Shortcode':
                            scode = el_item_sub.text
                        if el_item_sub.tag == 'Items':
                            for el_Items in el_item_sub:
                                for el_item2_sub in el_Items:
                                    if el_item2_sub.tag == 'Items':
                                        for el_Items2 in el_item2_sub:
                                            summary = self.dict_increment(summary, scode.replace(prefix_char1,''))
                    
        return self.summary_string('xml', summary)
