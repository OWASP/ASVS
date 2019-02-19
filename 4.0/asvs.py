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
from xml.sax.saxutils import escape
import csv

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


class ASVS:
    ''' Creates requirements list out of markdown files. '''
    requirements = []

    def __init__(self):
        for file in os.listdir("en"):

            if re.match("0x\d{2}-V", file):
                for line in open(os.path.join("en", file)):
                    regex = re.compile('\\*\\*([\d\.]+)\\*\\*\s\|\s{0,1}(.*?)\s{0,1}\|')
                    m = re.search(regex, line)
                    if m:
                        req = {}
                        req['id'] = m.group(1)
                        req['text'] = m.group(2)
                        req['file'] = file

                        self.requirements.append(req)

    def to_json(self):
        ''' Returns a JSON-formatted string '''
        return json.dumps(self.requirements)

    def to_xml(self):
        ''' Returns XML '''
        xml = ''

        for r in self.requirements:

            xml += "<requirement id = \"" + escape(r['id']) + "\">" + escape(r['text']) + "</requirement>\n"

        return xml

    def to_csv(self):
        ''' Returns CSV '''
        si = StringIO()

        writer = csv.DictWriter(si, ['id', 'text'])
        writer.writeheader()
        writer.writerows(self.requirements)

        return si.getvalue()
