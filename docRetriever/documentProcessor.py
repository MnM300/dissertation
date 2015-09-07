from Utilities import output_file
from xml.dom import minidom
from xmlParser import XMLParser
# from titleExtractor import get_section_titles, get_section_offset

# PMCIDS = "clinical diabetes"
# fulltexts = getFullText(PMCIDS)

# '23788751','24141372','21684626'

# print getAbstracts("clinical trials diabetes")


def make_output_mantime(body):
    '''It wraps the `body` with some XML code.

    '''
    xml_head = '<?xml version="1.0" encoding="UTF-8" ?>\n'
    xml_head += '<ClinicalNarrativeTemporalAnnotation>\n'
    xml_head += '<TEXT><![CDATA[\n'

    xml_footer = ']]></TEXT>\n'
    xml_footer += '<TAGS>\n'
    xml_footer += '</TAGS>\n'
    xml_footer += '</ClinicalNarrativeTemporalAnnotation>\n'
    return xml_head + body + xml_footer


def process_xml(text, filename):
    print('Processing {0}...'.format(filename))
    data = minidom.parseString(text)
    print 'Parsing document...'
    x = XMLParser(data.getElementsByTagName('body')[0])
    output_file('../ManTIME/input/{0}'.format(unicode(filename)),
                make_output_mantime(x.get_string()))
    # output_file('output/sections_{0}.xml'.format(unicode(filename)),
    #             get_section_offset(get_section_titles(text), x.get_string()).encode('utf-8'))
    output_file('../Medex/input/{0}'.format(unicode(filename)), x.get_string())


def process_txt(text, filename):
    print('Processing Corpus {0}'.format(filename))
    output_file('../ManTIME/input/{0}'.format(unicode(filename)),
                make_output_mantime(text))
    # output_file('output/sections_{0}.xml'.format(unicode(filename)),
    #             get_section_offset(get_section_titles(text), x.get_string()).encode('utf-8'))
    output_file('../Medex/input/{0}'.format(unicode(filename)), text)
