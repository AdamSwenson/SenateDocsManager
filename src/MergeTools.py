"""
Created by adam on 2/23/18
"""
__author__ = 'adam'



import os

from PyPDF2 import PdfFileReader, PdfFileMerger
import FileSystemTools as FST


def merge_pdfs(listOfFiles, exportFilePath):
    """Handles combining multiple pdfs.
    :param exportFilePath: The filename with path to the final consolidated file
    :type listOfFiles should have the base file as the first element.
    """
    if len(listOfFiles) is 0: return False

    # Merge the files
    merger = PdfFileMerger()

    for filename in listOfFiles:
        if filename[:-3] == 'pdf':
            merger.append(PdfFileReader(filename, 'rb'))

    merger.write(exportFilePath)



#
# filenames = FST.makeDataFileList(pathToFolder)
# print(pathToFolder, len(filenames))
