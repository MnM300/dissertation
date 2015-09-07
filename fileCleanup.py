import os
import shutil


def cleanup_medex():
    print 'Cleaning MedEX input'
    cleanup_directory('./Medex/input/')
    print 'Cleaning MedEX output'
    cleanup_directory('./Medex/output/')


def cleanup_mantime():
    print 'Cleaning ManTIME input'
    cleanup_directory('./ManTIME/input/')
    print 'Cleaning ManTIME output'
    cleanup_directory('./ManTIME/mantime/output/')


def cleanup_chronomaker():
    print 'Cleaning chronoMaker input'
    cleanup_directory('./input/')
    print 'Cleaning chronoMaker output'
    cleanup_directory('./output/')


def cleanup_directory(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
        except OSError, e:  # if failed, report it back to the user ##
                print ("Error: %s - %s." % (e.filename, e.strerror))


def backup_folder_contents(directory, destination):
    for filename in os.listdir(directory):
        source_path = os.path.join(directory, filename)
        destination_path = os.path.join(destination, filename)
        try:
            if os.path.isfile(source_path):
                shutil.copy(source_path, destination_path)
        except OSError, e:  # if failed, report it back to the user ##
                print ("Error: %s - %s." % (e.filename, e.strerror))

# cleanup_medex()
# cleanup_mantime()
# cleanup_chronomaker()

# backup_folder_contents('./temp/', './testremoval/')
# cleanup_directory('./testremoval/')
