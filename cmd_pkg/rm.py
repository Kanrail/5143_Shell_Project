import sys
import os

def rm(**kwargs):
    """
    RM                         User Commands                        RM
    NAME
        rm - deletes a file
    SYNOPSIS
        rm [FILE...]
    DESCRIPTION
        rm deletes a FILE. FILE must be existent, or function will return an
        error

    EXAMPLE
        rm file.txt

    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']

    try:
        paramPieces = []
        paramCharacters = list(str(params[0]))
        if '*' in paramCharacters: #checks for wildcard
            paramPieces = params[0].split('*') #breaks the string in half around wildcard
            fileList = []
            if len(paramPieces)>1: #if the wildcard was in the middle of string somewhere
                for root,dirs,files in os.walk(path[0]): #steps through filestructure of path
                    for file in files:
                        if file.startswith(paramPieces[0]) and file.endswith(paramPieces[1]):

                            os.remove(os.path.join(root,file))
                return ''

            if paramCharacters[0] is '*': #if the first character in params is wildcard
                for root,dirs,files in os.walk(path[0]):#steps through filestructure of path
                    for file in files:
                        if file.endswith(paramPieces[1]):
                            os.remove(os.path.join(root,file))
                return ''

            else: #if last character in params is wildcard
                for root,dirs,files in os.walk(path[0]):#steps through filestructure of path
                    for file in files:
                        if file.startswith(paramPieces[1]):
                            os.remove(os.path.join(root,file))
                return ''

        os.remove(path[0]+params[0])#fires if no wildcard present, just deletes file
        return ''
        
    except:
        return 'Invalid Input: No such file or directory\n'

if __name__=='__main__':
    sys.stdout.write(rm(params=['*txt'],path=['./testdir/']))
    pass
