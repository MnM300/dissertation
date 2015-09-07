from preProcessing import (get_sentence_timex_event_list)    # , get_sentence_offset)

from eventCount import (get_line_mention_totals,
                        get_percentage_occurances,
                        get_number_words,
                        get_table_mention,
                        get_event_header,
                        get_timex_header,
                        print_all_event_sums,
                        get_total_event_count,
                        get_total_timex_count,
                        get_all_event_sums,
                        get_all_timex_sums,
                        get_number_occurances)

from postMedexProcessor import (get_drug_offsets,
                                get_drug_count_per_sentence, remove_sentence_offsets)

from sentenceTokenizer import offset_lookup


def process_files(druglist_filename):
    print 'Processing file... ' + druglist_filename

    with open('../Medex/output/' + druglist_filename, 'r') as f:
        medex_output = f.read()

    with open('../Medex/input/' + druglist_filename, 'r') as f:
        plaintext = f.read()

    with open('../ManTIME/mantime/output/' + druglist_filename, 'r') as f:
        mantime_output = f.read()

    # sentence_offsets = get_sentence_offset(mantime_output)
    # sentence_offsets = get_sentence_offset(medex_output)
    sentence_offsets = offset_lookup(plaintext)

    sentence_events = get_sentence_timex_event_list(sentence_offsets, mantime_output)
    total_sentence_events = get_total_event_count(sentence_events)
    all_events = get_all_event_sums(sentence_events)
    total_sentence_timex = get_total_timex_count(sentence_events)
    all_timex = get_all_timex_sums(sentence_events)
    percentage_count = get_percentage_occurances(plaintext, sentence_offsets)
    line_mention_count = get_line_mention_totals(plaintext, sentence_offsets)
    word_count = get_number_words(mantime_output, sentence_offsets)
    number_count = get_number_occurances(plaintext, sentence_offsets)
    table_count = get_table_mention(plaintext, sentence_offsets)

    medex_output = remove_sentence_offsets(medex_output)

    drug_list = get_drug_offsets(medex_output)
    drug_count = get_drug_count_per_sentence(sentence_offsets, drug_list)

    with open('../output/' + druglist_filename + '.tsv', 'w') as f:
        header = 'SentenceID\t'
        header += 'WordCount\t'
        header += 'DrugCount\t'
        header += 'TotalEvents'
        header += str(get_event_header()) + '\t'
        header += 'TotalTimex'
        header += str(get_timex_header()) + '\t'
        header += 'NumPercentagePerSentence\t'
        header += 'NumFiguresPerSentence\t'
        header += 'NumKeywordMention-Line\t'
        header += 'TableCount\t'
        header += 'CLASS\n'

        f.write(header)

        # final = list(sentence_offsets)
        key_sentence_offsets = []
        str_output = ''
        valid_sentence = False
        for index, line in enumerate(sentence_offsets):

            if (int(drug_count[index]) >= 3 and
                    int(all_events[index][3]) >= 2 and    # PROBLEM
                    int(all_events[index][4]) >= 2):      # TREATMENT
                valid_sentence = True

            if (int(drug_count[index]) >= 3 and
                    int(all_events[index][4]) >= 4):      # TREATMENT
                valid_sentence = True

            if (int(percentage_count[index]) >= 2 and
                    int(number_count[index]) >= 2):
                valid_sentence = True

            if (int(percentage_count[index]) >= 2 and
                    int(all_events[index][3]) >= 3 and    # PROBLEM
                    int(all_events[index][4]) >= 2):      # TREATMENT
                valid_sentence = True

            if (int(line_mention_count[index]) >= 2 and
                    int(percentage_count[index]) >= 2):
                valid_sentence = True

            if (int(all_events[index][1]) >= 5 and        # EVIDENTIAL
                    int(all_events[index][3]) >= 3 and    # PROBLEM
                    int(all_events[index][4]) >= 3 and    # TREATMENT
                    int(percentage_count[index]) >= 3):
                valid_sentence = True

            if (int(drug_count[index]) >= 4 and
                    int(number_count[index]) < int(drug_count[index]) and
                    int(number_count[index]) >= 3):
                valid_sentence = True

            # if (int(word_count[index]) > 70):
            #     valid_sentence = False

            if (int(table_count[index]) >= 1 and        # EVIDENTIAL
                    int(word_count[index]) <= 60):
                valid_sentence = False
                print 'test'

            str_output += 's' + str(index + 1)
            str_output += '\t' + str(word_count[index])
            str_output += '\t' + str(drug_count[index])
            str_output += '\t' + str(total_sentence_events[index])
            str_output += str(print_all_event_sums(all_events[index]))
            str_output += '\t' + str(total_sentence_timex[index])
            str_output += str(print_all_event_sums(all_timex[index]))
            str_output += '\t' + str(percentage_count[index])
            str_output += '\t' + str(number_count[index])
            str_output += '\t' + str(line_mention_count[index])
            str_output += '\t' + str(table_count[index])
            # str_output += '\t' + '0' + '\n'
            # CREATES A COLUMN FOR THE CLASS OF THE DATA
            # IN ORDER TO RUN MACHINE LEARNING TECHNIQUES
            # TO VERIFY THE VALIDITY OF THE RULESET
            if (valid_sentence):
                key_sentence_offsets.append(line)
                str_output += '\t' + '1' + '\n'
            else:
                str_output += '\t' + '0' + '\n'

            valid_sentence = False

        f.write(str_output)

        key_sentence_offsets = list(set(key_sentence_offsets))

        print_key_sentences(plaintext, key_sentence_offsets, druglist_filename)

        #  with open('../Medex/input/' + druglist_filename, 'r') as f:
        #  print_key_sentences(f.read(), sentence_offsets, druglist_filename + '_full_list')


def print_key_sentences(plaintext, key_sentence_offsets, filename):
    out = ''
    for index, offset in enumerate(key_sentence_offsets):
        out += plaintext[int(offset.split('-')[0]) - 1:int(offset.split('-')[1])] + '\n\n'

        with open('../output/' + filename + '.txt', 'w') as f:
            f.write(out)
