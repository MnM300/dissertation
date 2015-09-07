from nltk.tokenize import sent_tokenize


def offset_lookup(raw_text):
    sentence_list = sent_tokenize(raw_text)

    offset_list = []
    for index, sent in enumerate(sentence_list):
        start = raw_text.index(sent)
        end = start + (len(sent) - 1)
        offset = str(start) + '-' + str(end)
        offset_list.append(offset)
        # test = str(index + 1) + '\t' + sent
        # print test
    return offset_list
