import sys
import os
from shutil import rmtree

def deleteItem(relPath, item, flag):
    try:
        if flag=='r': #r modifier for recursive destruction
            rmtree(relPath+item)
        else:
            rmdir(relPath+item)
    except:
        os.remove(relPath+item)


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

    OPTIONS
        -r  Recursively delete directories and files based on paramaters.

    EXAMPLE
        rm file.txt

    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']
    if 'tags' in kwargs:
        tags = kwargs['tags']

    try:
        paramPieces = []

        paramCharacters = list(str(params[0]))
        tagsCharacters = list(str(tags[0]))
        currentDirectory = os.listdir(path[0])
        tagFlag = ''

        if 'r' in tagsCharacters:
            tagFlag = 'r'
        if '*' in paramCharacters: #checks for wildcard
            paramPieces = params[0].split('*') #breaks the string in half around wildcard
            if params[0]=='*':
                #rmtree(path[0])
                for root,dirs,files in os.walk(path[0]): #steps through filestructure of path
                    for file in files:
                            os.remove(os.path.join(root,file))
                    for dir in dirs:
                        if tagFlag == 'r':
                            rmtree(os.path.relpath(os.path.join(root,dir), "."))
                        else:
                            rmdir(os.path.relpath(os.path.join(root,dir), "."))
                return ''
            elif '' not in paramPieces: #if the wildcard was in the middle of string somewhere
                for target in currentDirectory:
                    if target.startswith(paramPieces[0]) and target.endswith(paramPieces[1]):
                        deleteItem(path[0], target, tagFlag)
                return '' #end middle wildcard if statement

            elif paramPieces[0] is '': #if the first character in params is wildcard
                for target in currentDirectory:
                    if target.endswith(paramPieces[1]):
                        deleteItem(path[0], target, tagFlag)
                return '' #end first wildcard character statement

            else: #if last character in params is wildcard
                for target in currentDirectory:
                    if target.startswith(paramPieces[0]):
                        deleteItem(path[0], target, tagFlag)
                return ''#end last wildcard character statement
        deleteItem(path[0], params[0], tagFlag)#fires if no wildcard present, just deletes file
        return ''

    except:
        return 'Invalid Input: No such file or directory\n'

if __name__=='__main__':
    sys.stdout.write(rm(params=['test*'],path=['./testdir/testdir2/'],tags=['r']))
    pass
