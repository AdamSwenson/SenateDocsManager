"""
Utillities for exploring the filesystem
Created by adam on 12/27/16
"""
__author__ = 'adam'

import os


def getSystemRoot():
    """
    Returns the base directory path.
    This is usually: 'Users/adam/'
    """
    return os.getenv("HOME")


def makeDataFileList(folderPath, exclude=[]):
    """
    Returns a a list of all files in the source directory
    so that each file has its path appended to it.

    Args:
        folderPath: The path to get file names from
        exclude: file names which should not be included in the output list
    """
    exclude = exclude if any(exclude) else ['.DS_Store']
    datafiles = []
    for root, dirs, files in os.walk(folderPath):
        for name in files:
            if name not in exclude:
                datafiles.append(os.path.join(root, name))

    return datafiles


def makeDataFileIterator(folderPath, exclude=[]):
    """
    Returns an iterator of all files in the source directory
    so that each file has its path appended to it.

    Args:
        folderPath: The path to get file names from
        exclude: file names which should not be included in the output list
    """
    exclude = exclude if any(exclude) else ['.DS_Store']
    for root, dirs, files in os.walk(folderPath):
        for name in files:
            if name not in exclude:
                yield os.path.join(root, name)

     
def _get_file_name_from_path(self, path):
        """Parses out and returns the filename from the given path"""
        return path.split('/')[-1]
        
    
if __name__ == '__main__':
    pass
