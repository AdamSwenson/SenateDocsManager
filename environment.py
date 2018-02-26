"""
Created by adam on 2/26/18
"""
__author__ = 'adam'

import os


PROJECT_ROOT_FOLDER = os.getcwd()
TO_PROCESS = '%s/ToProcess' % PROJECT_ROOT_FOLDER
PROCESSED = '%s/Processed' % PROJECT_ROOT_FOLDER
OUTPUT = '%s/Output' % PROJECT_ROOT_FOLDER


"""Temporary storage for downloaded files"""
WORKING = '%s/tmp' % PROJECT_ROOT_FOLDER

# The string appended to the target file name by pdfx to create the
# temporary download folder
TEMP_DOWNLOAD_FOLDER_POSTFIX = '-referenced-pdfs'
