# Get list of files in to process directory
# file_iterator = FST.makeDataFileIterator(TO_PROCESS)

import FileSystemTools as FST
from environment import *


def download_pdfs(pathToBaseFile, workingPath):
    pdf = pdfx.PDFx(pathToBaseFile)
    metadata = pdf.get_metadata()
    references_list = pdf.get_references()
    references_dict = pdf.get_references_as_dict()
    pdf.download_pdfs(workingPath)


import pdfx
import PyPDF2


class Processor(object):

    def __init__(self):
        self.working_folder = WORKING
        self.output_folder = OUTPUT
        self.directory_to_process = TO_PROCESS
        # The string which pdfx will append to the end of the file name
        # in creating a folder to store the downloaded files in
        self.download_folder_postfix = TEMP_DOWNLOAD_FOLDER_POSTFIX

    def process_all(self):
        """Processes all files in the ToProcess directory"""
        for f in FST.makeDataFileIterator(self.directory_to_process):
            try:
                self.process_file(f)
            except:
                print("Error processing %s" % f)

    def process_file(self, originalPdfPath):
        print("\n ---- Preparing to process %s ---- " % self._get_file_name_from_path(originalPdfPath))

        self.pdf = pdfx.PDFx(originalPdfPath)

        # Download the files to the working directory
        self.pdf.download_pdfs(self.working_folder)

        # Loop through the downloaded pdfs, concatenating
        # them with the original
        self._merge_downloaded_files_with_original(originalPdfPath)

    def _get_file_name_from_path(self, objectPdf):
        """Since the incoming string will be a path, this parses out the filename"""
        return objectPdf.split('/')[-1]

    def _downloaded_docs_folder_name(self, objectPdf):
        """Parses out the file name of the original and since this
        will be used by the download library to form a new folder where
        the downloaded files are stored"""
        # extract the name from the path
        objectPdfName = self._get_file_name_from_path(objectPdf)
        return "%s/%s%s" % (self.working_folder, objectPdfName, self.download_folder_postfix)

    def _merge_downloaded_files_with_original(self, objectPdf):
        downloaded_files_folder = self._downloaded_docs_folder_name(objectPdf)
        exclude = []
        downloaded_file_iterator = FST.makeDataFileIterator(downloaded_files_folder, exclude)
        merger = PyPDF2.PdfFileMerger()

        # Push in the original file
        merger.append(objectPdf)

        # Loop through downloaded files, adding each
        for f in downloaded_file_iterator:
            merger.append(f)
            print("Merging in %s" % f)

        # Output the merged file
        output_path = "%s/%s" % (self.output_folder, self._get_file_name_from_path(objectPdf))
        merger.write(output_path)
        print("Saved merged file to %s" % output_path)
