import re
from preProcessing import offset_match_count


def get_drug_offsets(raw_text):
    if raw_text:
        drug_offsets = []
        for index, drug in enumerate(raw_text):
            drug_offsets.append(re.search('\d+,\d+', drug.split('|')[1]).group(0).replace(',', '-'))
        return drug_offsets


def get_drug_count_per_sentence(sentence_offsets, drug_offsets):
    drug_count = list(sentence_offsets)
    if sentence_offsets:
        for index, sentence in enumerate(sentence_offsets):
            drug_count[index] = offset_match_count(sentence, drug_offsets)
            # print drug_count[index]
    return drug_count


def remove_sentence_offsets(raw_text):
    pattern = '''<SENTENCE\s*(?:[^>"']|"[^"]*"|'[^']*')*?\sstart\s*=\s*"(\d+)"\s*end\s*=\s*"(\d+)" \/>'''
    return re.sub(pattern, '', raw_text).strip().split('\n')
