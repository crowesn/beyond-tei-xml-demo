#!/usr/bin/python3

# include required libraries

import csv
import xml.etree.ElementTree as ET
import sys
import re

# get file objects from cl
if len(sys.argv) == 3:
     teixml_input_file = open(sys.argv[1])
     csv_input_file = open(sys.argv[2])
else:
    sys.exit("Must include files with TEI and reference URIs")

outfilename = teixml_input_file.name + 'out.tei'

# parse files

xml = ET.parse(teixml_input_file)

# https://docs.python.org/2/library/xml.etree.elementtree.html#parsing-xml-with-namespaces
root = xml.getroot()

# get all name nodes
names = root.findall('.//name')

# next() skips the first row of the CSV file.
terms = csv.reader(csv_input_file)

terms_for_matching = dict(terms)

# iterate csv and xml and make replacements
for node in names:
    if node.text in terms_for_matching:
        node.attrib['ref'] = terms_for_matching[node.text]

# write to output file
xml.write(outfilename)

input("\n\n*** Updated xml saved to {0}, press <enter>").format(outfilename)
