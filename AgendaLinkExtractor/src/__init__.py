"""
Extracts all hyperlinks from each file
in the ToProcess folder, then downloads each
linked pdf and concatenates them with the original file.

Once complete
The completed file is outputed to Output and 
the original file is moved from ToProcess to Processed



"""

import os

import * from FileSystemTools

import pdfx

HOME = getSystemRoot()
PROJECT_ROOT_FOLDER = '%s/SenateDocsManager' % HOME
TO_PROCESS = '%s/ToProcess' % PROJECT_ROOT_FOLDER
PROCESSED = '%s/Processed' % PROJECT_ROOT_FOLDER
OUTPUT = '%s/Output' % PROJECT_ROOT_FOLDER

"""Temporary storage for downloaded files"""
WORKING = '%s/tmp' % PROJECT_ROOT_FOLDER

# The string appended to the target file name by pdfx to create the 
# temporary download folder
TEMP_DOWNLOAD_FOLDER_POSTFIX = '-referenced-pdfs'
