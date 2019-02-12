import sys

def tail (**kwargs):
    """
    TAIL                         User Commands                        TAIL
    NAME
        tail - displays bottom few lines of a file
    SYNOPSIS
        tail [FILE...]
    DESCRIPTION
        tail displays the bottom few lines of FILE to the terminal. Number of lines
        to be displayed can be specified with the -n tag.
    OPTIONS
        -n  specifies number of lines to be output starting from bottom of file
    EXAMPLE
        tail file.txt

    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']
    if 'tags' in kwargs:
        tags = kwargs['tags']

    try:
        finalLineList = []
        tempLineList = []
        try: #If the -n modifier is in use, tags[1] will be the number of lines
            numLines = int(tags[1])
        except: #default with no modifier
            numLines = 10
        fileIn = open(path[0]+params[0], 'r')
        for line in fileIn:
            tempLineList.append(line)
        endOfListPointer = len(tempLineList)-1
        while numLines > 0:
            finalLineList.insert(0,tempLineList[endOfListPointer])
            endOfListPointer-=1
            numLines-=1
        return finalLineList
    except:
        return 'Invalid Input: No such file or directory\n'

if __name__=='__main__':
    lineList = tail(path=['./'],params=['bacon.txt'],tags=['n',4])
    for item in lineList:
        sys.stdout.write(item)
    pass
