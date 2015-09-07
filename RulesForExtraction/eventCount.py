import re
from preProcessing import get_offsets, offset_match_count

_EVENTS_ = ["OCCURRENCE", "EVIDENTIAL", "TEST",
            "PROBLEM", "TREATMENT", "CLINICAL_DEPT"]

_TIMEX3_ = ["DATE", "TIME", "DURATION", "FREQUENCY"]

_SPOKEN_NUMBERS_ = ["first", "second", "third", "fourth", "fifth",
                    "sixth", "seventh", "eighth", "ninth", "tenth",
                    "eleventh", "twelfth", "thirteenth", "fourteenth",
                    "fifteenth", "sixteenth", "seventeenth"]

_SPECIAL_CASES_ = ['more', 'multy', 'multi', 'therapy', 'many']


# GET THE COUNT OF ALL EVENTS PER SENTENCE
def get_event_count(event_type, event_list):
    events = event_list.split(',')
    count = 0
    for index, event in enumerate(events):
        if(event == event_type):
            count += 1
    return count


def get_all_event_sums(sentence_events):
    event_totals = []
    event_total = list(_EVENTS_)
    for index, sentence_event in enumerate(sentence_events):
        event_total = list(_EVENTS_)
        # sentence_event = str(sentence_event).split('|')[0].split(':')[1] if sentence_event).split('|')[0].split(':')[0] != 0 else ''
        sentence_event = str(sentence_event).split('|')[1].split(':')[1] if str(sentence_event).split('|')[1].split(':')[0] != '0' else ''
        for index, eventType in enumerate(_EVENTS_):
            event_total[index] = get_event_count(eventType, sentence_event)
        event_totals.append(event_total)
    return event_totals


def get_all_timex_sums(sentence_events):
    event_totals = []
    for index, sentence_event in enumerate(sentence_events):
        event_total = list(_TIMEX3_)
        sentence_event = str(sentence_event).split('|')[0].split(':')[1] if str(sentence_event).split('|')[0].split(':')[0] != '0' else ''
        # sentence_event = str(sentence_event).split('|')[1].split(':')[1] if str(sentence_event).split('|')[1].split(':')[0] != '0' else ''
        for index, eventType in enumerate(_TIMEX3_):
            event_total[index] = get_event_count(eventType, sentence_event)
        event_totals.append(event_total)
    return event_totals


def print_all_event_sums(all_events):
    event = ''

    for index, columns in enumerate(all_events):
        event += '\t' + str(columns)
    return event


# GET THE TOTAL COUNT OF EVENTS PER SENTENCE
def get_total_timex_count(sentence_events):
    total_timex = list(sentence_events)
    for index, events in enumerate(total_timex):
        total_timex[index] = str(events).split('|')[0].split(':')[0]
    return total_timex


def get_total_event_count(sentence_events):
    total_event = list(sentence_events)
    for index, events in enumerate(total_event):
        total_event[index] = str(events).split('|')[1].split(':')[0]
    return total_event


# GET THE NUMBER % OCURRENCES IN A SINGLE SENTENCE
def get_percentage_occurances(raw_text, sentence_offsets):
    total_percentage_count = list(sentence_offsets)
    pattern = '\d{1,3}\.?\d{1,3}?\s?\%'
    for index, offset in enumerate(total_percentage_count):
        offsets = str(offset).split('-')
        str_output = raw_text[int(offsets[0]):int(offsets[1])]
        total_percentage_count[index] = len(re.findall(pattern, str_output))
    return total_percentage_count


def get_number_occurances(raw_text, sentence_offsets):
    total_number_count = list(sentence_offsets)
    pattern = '(?<![a-z])([-+.]?\d+[\,\.]?\d+)(?!%)(?!\s%)'
    for index, offset in enumerate(total_number_count):
        offsets = str(offset).split('-')
        str_output = raw_text[int(offsets[0]):int(offsets[1])]
        total_number_count[index] = len(re.findall(pattern, str_output))
    return total_number_count


def get_table_mention(raw_text, sentence_offsets):
    table_count = list(sentence_offsets)
    pattern = 'Table'
    for index, offset in enumerate(table_count):
        offsets = str(offset).split('-')
        str_output = raw_text[int(offsets[0]):int(offsets[1])]
        table_count[index] = len(re.findall(pattern, str_output))
    return table_count


#  Not being used
def get_line_mentions(raw_text):
    pattern = '\w+(?=\Wline)'
    return re.findall(pattern, raw_text)


def filter_line_mentions(line_mentions):
    count = 0
    for index, mention in enumerate(line_mentions):
        if mention in _SPOKEN_NUMBERS_:
            count += 1
        elif mention in _SPECIAL_CASES_:
            count += 1
    return count


def get_line_mention_totals(raw_text, sentence_offsets):
    total_line_mention_count = list(sentence_offsets)
    pattern = '\w+(?=\Wline)'
    for index, offset in enumerate(total_line_mention_count):
        offsets = unicode(offset).split('-')
        str_output = raw_text[int(offsets[0]):int(offsets[1])]
        total_line_mention_count[index] = filter_line_mentions(re.findall(pattern, str_output))
    return total_line_mention_count


def get_event_header():
    event_header = ''
    for index, event in enumerate(_EVENTS_):
        event_header += '\t' + event
    return event_header


def get_timex_header():
    timex_header = ''
    for index, timex in enumerate(_TIMEX3_):
        timex_header += '\t' + timex
    return timex_header


def get_number_words(raw_text, sentence_offsets):
    pattern = '''<WORD (?:[^>"']|"[^"]*"|'[^']*')+?\sstart\s*=\s*"(\d+)"'''
    pattern += '''\s*end\s*=\s*"(\d+)"(?:[^>"']|"[^"]*"|'[^']*')+? \/>'''
    word_offsets = get_offsets(raw_text, pattern)
    word_count = list(sentence_offsets)
    if sentence_offsets:
        for index, sentence in enumerate(sentence_offsets):
            word_count[index] = offset_match_count(sentence, word_offsets)
    return word_count
