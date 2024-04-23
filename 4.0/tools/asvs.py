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
import base64
import urllib.request
import datetime
from xml.sax.saxutils import escape
import csv
from dicttoxml2 import dicttoxml
import xml.etree.ElementTree as ET
from marko.ext.gfm import gfm

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class ASVS:
    asvs = {}
    asvs['Name'] = "Application Security Verification Standard Project"
    asvs['ShortName'] = "ASVS"
    asvs['Version'] = ""
    asvs['Description'] = ("The OWASP Application Security Verification Standard (ASVS) Project "
            "provides a basis for testing web application technical security controls and also "
            "provides developers with a list of requirements for secure development.")

    asvs_flat = {}
    asvs_flat2 = {}
    asvs_flat['requirements'] = []
    asvs_flat2['requirements'] = []
    language = ''

    rv = json.load(open(os.path.join("templates", "ReqView-ASVS.reqw"), encoding="utf8"))

    def __init__(self, language_in):

        self.language = language_in
        prefix_char1, prefix_char2, prefix_char1_b = self.get_prefix()

        regex = re.compile(r'Version (([\d.]+){3})')

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
                self.rv['description'] = m.group(1)

        nist_url = "https://pages.nist.gov/800-63-3/sp800-63b.html"
        nist_html = urllib.request.urlopen(nist_url).read().decode()
        nist_headings = ["".join(h) for h in re.findall(r'<h[34]([^>]*)>(.+)</h[34]>', nist_html)]
        nist_map = {}
        for h in nist_headings:
            if secnum := re.findall(r'[1-9A]+\.[0-9\.]+', h):
                if a_id := re.findall(r'id="(.+)"', h):
                    nist_map[secnum[0]] = a_id[0]
                if a_name := re.findall(r'name="(.+)"', h):
                    nist_map[secnum[0]] = a_name[0]

        self.asvs['Requirements'] = chapters = []
        rv_doc = self.rv['documents'][0]
        timestamp = datetime.datetime.now(datetime.UTC).isoformat(timespec='milliseconds')[:-6] + "Z"
        rv_doc['createdOn'] = rv_doc['lastChangedOn'] = timestamp

        rv_chapters = rv_doc['data'] = []
        if self.language == 'ar':
            rv_doc['rtl'] = True

        self.rv['attachments'] = {}
        rv_stack = [rv_chapters]

        rv_level = 0

        def rv_parse_md(file, stack, level):
            doc = gfm.parse(open(os.path.join(self.language, file), encoding="utf8").read())
            obj = None
            for e in doc.children:
                t = e.get_type()
                if t == "Heading":
                    if not e.children:
                        continue
                    h_obj = {
                        'heading': e.children[0].children,
                        'children': [],
                        'type': 'INFO'
                    }
                    obj = None
                    if e.level > level:
                        level += 1
                    else:
                        while e.level < level:
                            stack.pop()
                            level -= 1
                        if e.level == level:
                            stack.pop()
                    stack[-1].append(h_obj)
                    stack.append(h_obj['children'])
                elif t != "BlankLine":
                    if obj is None:
                        obj = {
                            'text': "",
                            'type': 'INFO'
                        }
                        stack[-1].append(obj)
                    if e.children:
                        for img in [c for c in e.children if c.get_type() == "Image"]:
                            if img.dest.startswith("https://"):
                                stream = urllib.request.urlopen(img.dest)
                            else:
                                stream = open(os.path.join(self.language, img.dest), "rb")
                            att_id = os.path.basename(img.dest)
                            if 'attachments' not in obj:
                                obj['attachments'] = []
                            obj['attachments'].append(att_id)
                            b64_data = base64.b64encode(stream.read())
                            self.rv['attachments'][att_id] = {'data': f"data:image/png;base64,{b64_data.decode()}"}

                        e.children = [c for c in e.children if c.get_type() != "Image"]
                    html = gfm.render(e)
                    if html and html != "<p></p>\n":
                        obj['text'] += self.rv_html(html)
            return level

        for file in sorted(os.listdir(self.language)):

            if re.match(r"0x0\d-.+\.md$", file):
                rv_level = rv_parse_md(file, rv_stack, rv_level)

            if re.match(r"0x\d{2}-V", file):
                chapter = {}
                chapter['Shortcode'] = ""
                chapter['Ordinal'] = ""
                chapter['ShortName'] = ""
                chapter['Name'] = ""
                chapter['Items'] = []

                # never used by rv
                rv_chapter = {
                    'type': 'CHAP',
                    'asvsId': "",
                    'ord': "",
                    'heading': "",  # ShortName
                    'children': []
                }

                section = {}
                section['Shortcode'] = ""
                section['Ordinal'] = ""
                section['Name'] = ""
                section['Items'] = []

                # never used by rv
                rv_section = {
                    'type': 'SEC',
                    'shortcode': "",
                    'ord': "",
                    'heading': "",  # Name
                    'children': []
                }

                regex = re.compile(r'0x\d{2}-(V([0-9]{1,3}))-(\w[^-.]*)')
                m = re.search(regex, file)
                if m:
                    chapter = {}
                    chapter['Shortcode'] = m.group(1).replace('V', prefix_char1)
                    chapter['Ordinal'] = int(m.group(2))
                    chapter['ShortName'] = m.group(3)
                    chapter['Name'] = ""
                    chapter['Items'] = []

                    rv_chapter = {
                        'type': 'CHAP',
                        'asvsId': chapter['Shortcode'][1:],
                        'ord': chapter['Ordinal'],
                        'heading': chapter['ShortName'],
                        'children': []
                    }

                    section = {}
                    section['Shortcode'] = m.group(1).replace('V', prefix_char1)
                    section['Ordinal'] = int(m.group(2))
                    section['Name'] = m.group(3)
                    section['Items'] = []

                    rv_section = {
                        'type': 'SEC',
                        'asvsId': section['Shortcode'][1:],
                        'ord': section['Ordinal'],
                        'heading': section['Name'],
                        'children': []
                    }

                    chapters.append(chapter)
                    rv_chapters.append(rv_chapter)

                rv_chapter_help_lines = []
                rv_section_help_lines = []
                rv_help_dest = None
                def rv_push_help_line(line):
                    if rv_help_dest and line and not line.startswith("| # |") and line.count(":---") < 6:
                        arr = rv_chapter_help_lines if rv_help_dest == 'chapter' else rv_section_help_lines
                        arr.append(line)
                def rv_render_help():
                    if not rv_help_dest:
                        return
                    arr = rv_chapter_help_lines if rv_help_dest == 'chapter' else rv_section_help_lines
                    if not arr:
                        return
                    lines = "".join(arr)
                    arr.clear()
                    help_text = self.rv_html(gfm(lines), True)
                    if rv_help_dest == 'chapter':
                        rv_chapter['help'] = rv_chapter.get('help', '') + help_text
                    else:
                        rv_section['help'] = rv_section.get('help', '') + help_text

                for line in open(os.path.join(self.language, file), encoding="utf8"):
                    found_regex = False
                    regex = re.compile(r"^#\s(" + prefix_char1 + "([0-9]{1,2})" + prefix_char1_b + r")\s([\w\s][^\n]*)")
                    #if line.startswith('# '):
                    #    print(line)
                    m = re.search(regex, line)
                    if m:
                        rv_render_help()
                        rv_help_dest = 'chapter'
                        found_regex = True
                        chapter['Name'] = m.group(3)
                        rv_chapter['heading'] = chapter['Name']

                    regex = re.compile("## (" + prefix_char2 + r"[0-9]{1,2}.([0-9]{1,3})) ([\w\s][^\n]*)")
                    m = re.search(regex, line)
                    if m:
                        rv_render_help()
                        rv_help_dest = 'section'
                        found_regex = True
                        section = {}
                        section['Shortcode'] = m.group(1)
                        section['Ordinal'] = int(m.group(2))

                        if self.language == 'ar':
                            section['Ordinal'] = int(m.group(1).split('.')[0].replace(prefix_char2, ''))

                        section['Name'] = m.group(3)
                        section['Items'] = []

                        rv_section = {
                            'type': 'SEC',
                            'asvsId': section['Shortcode'][1:],
                            'ord': section['Ordinal'],
                            'heading': section['Name'],
                            'children': []
                        }

                        chapter['Items'].append(section)
                        rv_chapter['children'].append(rv_section)

                    regex = re.compile(r"\*\*([\d\.]+)\*\*\s\|\s{0,1}(.*?)\s{0,1}\|(.*?)\|" +
                                    r"(.*?)\|(.*?)\|([0-9,\s]*)\|([A-Z0-9/\s,.]*)\|{0,1}")
                    m = re.search(regex, line)
                    if m:
                        found_regex = True
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

                        rv_req = {
                            'type': 'REQ',
                            'asvsId': req['Shortcode'][1:],
                            'ord': req['Ordinal'],
                            'text': self.rv_html(gfm(req['Description'])),
                            'applicable': True
                        }
                        rv_cwe = ", ".join([f'<a href="https://cwe.mitre.org/data/definitions/{n}.html">{n}</a>' for n in req['CWE']])
                        if rv_cwe:
                            rv_req['cwe'] = "<p>" + rv_cwe + "</p>"
                        rv_nist = " / ".join([f'<a href="{nist_url}#{nist_map.get(s, "")}">{s}</a>' for s in req['NIST']])
                        if rv_nist:
                            rv_req['nist'] = "<p>" + rv_nist + "</p>"
                        if req['Description'].startswith("[DELETED"):
                            rv_req['deleted'] = True
                        if level1['Requirement'] == "Optional":
                            rv_req['l1'] = "OPT"
                            rv_req['l1text'] = "o"
                        elif level1['Required']:
                            rv_req['l1'] = "REQ"
                            rv_req['l1text'] = level1['Requirement']
                        else:
                            rv_req['l1'] = "NREQ"

                        if level2['Requirement'] == "Optional":
                            rv_req['l2'] = "OPT"
                            rv_req['l2text'] = "o"
                        elif level2['Required']:
                            rv_req['l2'] = "REQ"
                            rv_req['l2text'] = level2['Requirement']
                        else:
                            rv_req['l2'] = "NREQ"

                        if level3['Requirement'] == "Optional":
                            rv_req['l3'] = "OPT"
                            rv_req['l3text'] = "o"
                        elif level3['Required']:
                            rv_req['l3'] = "REQ"
                            rv_req['l3text'] = level3['Requirement']
                        else:
                            rv_req['l3'] = "NREQ"

                        section['Items'].append(req)
                        rv_section['children'].append(rv_req)
                        self.asvs_flat['requirements'].append(req_flat)
                        self.asvs_flat2['requirements'].append(req_flat2)

                    if not found_regex:
                        if re.findall(r'^#+\s', line):
                            rv_render_help()
                            if rv_help_dest == 'section':
                                rv_help_dest = 'chapter'
                        rv_push_help_line(line)

                rv_render_help()
                rv_help_dest = None

            if re.match(r"0x9\d-", file):
                rv_level = rv_parse_md(file, rv_stack, rv_level)


    def rv_html(self, html, is_help = False):
        html = html.replace("\n", "")
        if is_help:
            def heading_sub(m):
                tag = 'em' if int(m.group(2)) > 2 else 'strong'
                if m.group(1):
                    return f'</{tag}></p>'
                else:
                    return f'<p><{tag}>'
            html = re.sub(r'<(/?)h(\d)>', heading_sub, html)
        if self.language != "ar":
            return html.replace('<table>', '<table style="width: 100%;">').strip()
        def rtl_sub(m):
            tag = m.group(1)
            table_width = ' style="width: 100%;"' if tag == "table" else ""
            return f'<{tag} dir="rtl"{table_width}>'
        return re.sub(r'<(p|[uo]l|table)>', rtl_sub, html).strip()

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

    def to_reqw_json(self):
        return json.dumps(self.rv, indent = 2, sort_keys = False, ensure_ascii=False).strip()

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
