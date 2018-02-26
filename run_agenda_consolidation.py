"""
Extracts all hyperlinks from each file
in the ToProcess folder, then downloads each
linked pdf and concatenates them with the original file.

Once complete
The completed file is outputed to Output and 
the original file is moved from ToProcess to Processed



"""
import os
from src import FileSystemTools as FST
from src import MergeTools as MT
from src import ExtractionService as ES

from environment import *
from src.ExtractionService import Processor

# HOME = FST.getSystemRoot()
# PROJECT_ROOT_FOLDER = os.getcwd()
# TO_PROCESS = '%s/ToProcess' % PROJECT_ROOT_FOLDER
# PROCESSED = '%s/Processed' % PROJECT_ROOT_FOLDER
# OUTPUT = '%s/Output' % PROJECT_ROOT_FOLDER

# get the files to process
fileNames = FST.makeDataFileList(TO_PROCESS)
print("%s files" % len(fileNames))

p = Processor()
p.process_all()

#
# for f in fileNames:
#     tempFolderName = "%s/%s" % (WORKING, f)  # FST.get_temp_directory_for_job(f)
#     # download
#     ES.download_pdfs(f, tempFolderName)
#     output = "%s/%s" % (PROCESSED, f)
#     # combine into one file
#     MT.merge_pdfs(tempFolderName, output)
