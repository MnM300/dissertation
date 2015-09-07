#!/usr/bin/env python
#
#   Copyright 2015 Michele Filannino, Rondy Monnaie
#
#   gnTEAM, School of Computer Science, University of Manchester.
#   All rights reserved. This program and the accompanying materials
#   are made available under the terms of the GNU General Public License.
#
#   author: Michele Filannino, Rondy Monnaie
#   email:  filannim@cs.man.ac.uk, rondy.monnaie@postgrad.manchester.ac.uk
#
#   For details, send us an email. :)

import xml.etree.cElementTree as etree
import re


# pmcids = ['4084583', '4164026', '4079914']
def get_section_titles(xml):
    doc = etree.fromstring(xml)
    namespace = '{http://dtd.nlm.nih.gov/2.0/xsd/archivearticle}'
    titles = doc.findall('.//{0}body/{0}sec/{0}title'.format(namespace))
    return [title.text for title in titles]


def get_title_offset(titles, text):
    title_offsets = ''
    print 'Retrieving Section titles Offsets...'
    for title in titles:
        offset = re.search(title, text)
        if offset:
            title_offsets += unicode(title) + '\t'
            title_offsets += unicode(offset.start()) + '\t'
            title_offsets += unicode(offset.end()) + '\n'
    return title_offsets


def get_section_offset(titles, text):
    title_offsets = ''
    for index, title in enumerate(titles):
        current_offset = re.search(titles[index].encode('utf-8'), text)
        title_offsets += unicode(title) + '\t'
        title_offsets += unicode(current_offset.end() + 1) + '\t'
        if index < len(titles) - 1:
            next_offset = re.search(titles[index + 1].encode('utf-8'), text)
            title_offsets += unicode(next_offset.start() - 1) + '\n'
        else:
            title_offsets += unicode(len(text) - 1) + '\n'
    return title_offsets


'''
import xml.etree.cElementTree as etree
from OAI import get_fulltext_by_uids


# pmcids = ['4084583', '4164026', '4079914']
def get_section_titles(pmcids):
    for xml_id, xml in enumerate(xml_list=get_fulltext_by_uids(pmcids)):
        doc = etree.fromstring(xml)
        titles = doc.findall('.//{http://dtd.nlm.nih.gov/2.0/xsd/archivearticle}title')
        print xml_id, [title.text for title in titles]
'''
