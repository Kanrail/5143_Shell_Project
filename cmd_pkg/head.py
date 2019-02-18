import sys

def head (**kwargs):
    """
    HEAD                         User Commands                        HEAD
    NAME
        head - displays top few lines of a file
    SYNOPSIS
        head [FILE...]
    DESCRIPTION
        head displays the top few lines of FILE to the terminal. Number of lines
        to be displayed can be specified with the -n tag.
    OPTIONS
        -n  specifies number of lines to be output starting from top of file
    EXAMPLE
        head file.txt

    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']
    if 'tags' in kwargs:
        tags = kwargs['tags']

    try:
        lineList = []
        try: #If the -n modifier is in use, tags[1] will be the number of lines
            numLines = int(tags[1])
        except: #default with no modifier
            numLines = 10
        fileIn = open(path[0]+params[0], 'r')
        while numLines > 0: #appends to a list the number of lines in variable n
            lineList.append(fileIn.readline())
            numLines-=1
        return lineList
    except: #General error handling
        return 'Invalid Input: No such file or directory\n'

if __name__=='__main__':
    lineList = head(path=['./'],params=['bacon.txt'],tags=['n',4])
    for item in lineList:
        sys.stdout.write(item)
    pass
