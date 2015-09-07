import re


# OFFSET RETRIEVAL
def get_offsets(raw_text, pattern):
    offsets = re.findall(pattern, raw_text)
    if offsets:
        for index, offset in enumerate(offsets):
            offsets[index] = offset[0] + '-' + offset[1]
    return offsets


# OFFSET AND TYPE RETRIEVAL
def get_offset_type(raw_text, pattern):
    offsets = re.findall(pattern, raw_text)
    if offsets:
        for index, offset in enumerate(offsets):
            offsets[index] = offset[0] + '-' + offset[1] + '-' + offset[2].strip('"')
    return offsets


# OFFSET RANGE VALIDATION
def range_check(srange, svalue):
    srange = srange.split('-')
    svalue = svalue.split('-')
    if int(svalue[0]) < int(svalue[1]):
        return (int(srange[0]) <= int(svalue[0]) <= int(srange[1])) and (int(srange[0]) <= int(svalue[1]) <= int(srange[1]))
    else:
        print 'Invalid Range: ' + svalue[0] + '-' + svalue[1]
        return False


# EVENT OFFSET MATCHING
def offset_match(sentence_offsets, type_offsets):
    type_list = list(sentence_offsets)
    if sentence_offsets:
        for index, sOffsets in enumerate(sentence_offsets):
            if type_offsets:
                # eventList=str(index+1) + ','
                offset_list = ''
                for index2, offsets in enumerate(type_offsets):
                    if range_check(sOffsets, offsets):
                        offsets = offsets.split('-')
                        offset_list += str(offsets[2]) + ','
                offset_list = offset_list.rstrip(',')
                type_list[index] = offset_list
            else:
                print 'No Offsets Found'
        return type_list
    else:
        print 'No Sentence Offsets Found'
        return 0


# EVENT OFFSET COUNT PER SENTENCE
def offset_match_count(sentence_offset, type_offsets):
    count = 0
    if type_offsets:
        for index, offset in enumerate(type_offsets):
            if range_check(sentence_offset, offset):
                count += 1
        return count
    else:
        print 'No Offsets Found'
        return 0


# SENTENCE OFFSET RETRIEVAL
def get_sentence_offset(raw_text):
    pattern = '''<SENTENCE\s*(?:[^>"']|"[^"]*"|'[^']*')*?\sstart\s*=\s*"(\d+)"\s*end\s*=\s*"(\d+)" \/>'''
    return get_offsets(raw_text, pattern)


# EVENT OFFSET RETRIEVAL
def get_event_offset(raw_text):
    pattern = '''<EVENT(?:[^>"']|"[^"]*"|'[^']*')+?\sstart\s*=\s*"(\d+)"\s*end\s*=\s*"'''
    pattern += '''(\d+)"(?:[^>"']|"[^"]*"|'[^']*')+?type\s*=\s*([^>"']|"[^"]*"|'[^']*')* \/>'''
    return get_offset_type(raw_text, pattern)


# TIMEX3 OFFSET RETRIEVAL
def get_timex_offset(raw_text):
    pattern = '''<TIMEX3(?:[^>"']|"[^"]*"|'[^']*')+?\sstart\s*=\s*"(\d+)"\s*end\s*=\s*"'''
    pattern += '''(\d+)"(?:[^>"']|"[^"]*"|'[^']*')+?type\s*=\s*([^>"']|"[^"]*"|'[^']*').* \/>'''
    return get_offset_type(raw_text, pattern)


# EVENT OFFSET MATCHING
def get_event_list(sentence_offsets, raw_text):
    return offset_match(sentence_offsets, get_event_offset(raw_text))


# TIMEX3 OFFSET MATCHING
def get_timex_list(sentence_offsets, raw_text):
    return offset_match(sentence_offsets, get_timex_offset(raw_text))


# AGGREGATE COUNT AND STRING OF list items
def content_aggregation(content):
    return (str(len(content.split(','))) + ':' if content.split(',')[0] != '' else '0') + content


#  OUTPUT:  TIMEX3 COUNT: TIMEX3 TYPES | EVENT COUNT: EVENT TYPES E.G. '1:"DURATION"|2:"PROBLEM","TREATMENT"'
def get_sentence_timex_event_list(sentence_offsets, raw_text):
    sentence_events = list(sentence_offsets)
    event_type_list = get_event_list(sentence_offsets, raw_text)
    timex3_type_list = get_timex_list(sentence_offsets, raw_text)

    for index, events in enumerate(sentence_events):
        sentence_events[index] = str(content_aggregation(timex3_type_list[index])) + '|' + str(content_aggregation(event_type_list[index]))
    return sentence_events


def get_sentence_timex_list(sentence_offsets, raw_text):
    sentence_events = list(sentence_offsets)
    timex3_type_list = get_timex_list(sentence_offsets, raw_text)

    for index, events in enumerate(sentence_events):
        sentence_events[index] = str(content_aggregation(timex3_type_list[index]))
    return sentence_events


def get_sentence_event_list(sentence_offsets, raw_text):
    sentence_events = list(sentence_offsets)
    event_type_list = get_event_list(sentence_offsets, raw_text)

    for index, events in enumerate(sentence_events):
        sentence_events[index] = str(content_aggregation(event_type_list[index]))
    return sentence_events


#  GET COUNTS
def get_total_sentence_events(sentence_offsets, raw_text):
    total_events = list(sentence_offsets)
    all_events = get_event_offset(raw_text)
    if sentence_offsets:
        for index, sOffset in enumerate(sentence_offsets):
            total_events[index] = offset_match_count(sOffset, all_events)
        return total_events
    else:
        print 'No Sentence Offsets Found'
        return 0


def get_total_sentence_timex(sentence_offsets, raw_text):
    total_events = list(sentence_offsets)
    all_events = get_timex_offset(raw_text)
    if sentence_offsets:
        for index, sOffset in enumerate(sentence_offsets):
            total_events[index] = offset_match_count(sOffset, all_events)
        return total_events
    else:
        print 'No TIMEX3 Offsets Found'
        return 0
