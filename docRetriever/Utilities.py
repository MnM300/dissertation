import urllib2
import codecs


# Output string data to a file
def output_file(filename, output_data):
    with open(filename, "w") as data_output:
        data_output.write(output_data)


# append string data to a file
def append_file(filename, append_data):
    with codecs.open(filename, "a", encoding='utf8') as data_output:
        data_output.write(append_data.encode('utf8'))


# Retrieve ouput from given url
def get_url_response(url1, url2):
    return urllib2.urlopen(url1 + url2).read()


# convert List to single string
def list_to_string(my_list):
    final_string = ""
    for listItem in my_list:
        final_string += listItem + ', '
    return final_string.strip().rstrip(',')
