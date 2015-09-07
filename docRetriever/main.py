import os
import re
import errno
from documentProcessor import process_txt, process_xml
from OAI import get_fulltext_by_uids, get_fulltext
from Utilities import output_file


def get_papers_from_file():
    path = "../input/"

    for filename in os.listdir(path):
        if filename.endswith(".xml"):
            try:
                with open(path + filename) as f:
                    process_xml(f.read(), filename)
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise
        elif filename.endswith(".txt"):
            try:
                with open(path + filename) as f:
                    process_txt(f.read(), filename)
            except IOError as exc:
                if exc.errno != errno.EISDIR:
                    raise


def get_pmcid_from_raw_xml(raw_xml):
    pmcids = re.findall('<article-id pub-id-type="pmcid">(.*?)</article-id>', raw_xml, re.DOTALL)
    return pmcids


def get_papers_from_search_criteria(search_criteria):
    fulltexts = get_fulltext(search_criteria)

    if fulltexts:
        for text_id, text in enumerate(fulltexts):
            pmcid = get_pmcid_from_raw_xml(text)
            filename = unicode(pmcid[0]) + '.xml'
            output_file('../input/{0}'.format(filename), text)
            process_xml(text, filename)
    else:
        print 'No records Found on PubMed Central for {0}'.format(search_criteria)


def get_papers_from_pmcids(pmcids):
    fulltexts = get_fulltext_by_uids(pmcids)

    if fulltexts:
        for text_id, text in enumerate(fulltexts):
            print text
            pmcid = get_pmcid_from_raw_xml(text)
            filename = unicode(pmcid[0]) + '.xml'
            output_file('../input/{0}'.format(filename), text)
            process_xml(text, filename)
    else:
        print 'No records Found on PubMed Central for {0}'.format(pmcids)

# PMCIDS = ['3381956', '3244351', '3707340', '4367711', '3575628', '3377519', '4209383']
# PMCIDS = ['4084583', '4164026', '4079914', 24141372, 21684626, 23788751]
# get_papers_from_pmcids(PMCIDS)
