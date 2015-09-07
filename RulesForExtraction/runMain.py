import os
import errno
from main import process_files

path = "../ManTIME/mantime/output/"

for filename in os.listdir(path):
    if filename.endswith(".xml"):
        print('Opening file {0} ...'.format(filename))
        try:
            # with open(path + filename) as f:
            #    process_files(f.read(), filename)
            process_files(filename)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
    if filename.endswith(".txt"):
        print('Opening file {0} ...'.format(filename))
        try:
            # with open(path + filename) as f:
            #    process_files(f.read(), filename)
            process_files(filename)
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise
