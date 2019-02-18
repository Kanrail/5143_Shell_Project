import sys
import glob
import os

def grepL(**kwargs):
    """
    Function Name: grepL
    Input: params (keyword to match to)
    Output: fileList (list of matching filenames)
    Description: params contains a keyword to search the filenames that are in path and returns
    a list of those that contain the keyword. Also returns any directories with the tag that it is
    a directory and thus won't search it.
    """
    if 'params' in kwargs:
        params = kwargs['params']
    path = glob.glob(os.path.join('*'))
    fileList = []

    for file in path:
        try:
            paramFound = False
            inputFile = open(file)
            for line in inputFile:
                if params[0] in line:
                    paramFound = True
                    break
            if paramFound == True:
                fileList.append(file)
        except:
            fileList.append(file+' is a directory')
    return fileList

def grep (**kwargs):
        """
    GREP                         User Commands                        GREP
    NAME
        grep - print lines that match patterns
    SYNOPSIS
        grep PATTERNS [FILE...]
    DESCRIPTION
        grep searches for PATTERNS in each FILE.  PATTERNS is one or patterns
        separated by newline characters, and grep prints each line that
        matches a pattern.
        If no FILE is given,it will return an error.

    EXAMPLE
        grep 'word' file.txt

    """
        if 'params' in kwargs:
            params = kwargs['params']
        if 'path' in kwargs:
            path = kwargs['path']
        if 'tags' in kwargs:
            tags = kwargs['tags']
        else:
            tags = []

        try:
            if not tags:
                inputFile = open(path[1]+params[1])
                retStringList = []
                for line in inputFile:
                    if params[0] in line:
                        retStringList.append(line)
                return retStringList
            elif tags[0]=='l':
                return grepL(params=params)

        except:
            return 'Invalid Input: No such file or directory'

if __name__=='__main__':
    grepReturn = grep(params=['bacon','bacon.txt'], path=['./','../'])
    for line in grepReturn:
        sys.stdout.write(line)
    pass
