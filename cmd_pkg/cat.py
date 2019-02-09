import sys

def cat (**kwargs):
    """
    CAT                         User Commands                        CAT
    NAME
        cat - concatinates files
    SYNOPSIS
        cat [FILE...] [FILE2...] ... [FILEn...]
    DESCRIPTION
        cat displays a FILE as if concatinated to any number of other FILEs
        sequentually in order after the command and displays them to the screen.
        All FILEs used must exist

    EXAMPLE
        cat file.txt file2.txt
        cat file.txt , file2.txt
        cat file.txt
    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']

    try:
        pathCounter = 0
        stringList = []
        for param in params:
            tempFile = open(path[pathCounter]+param)
            for line in tempFile:
                stringList.append(line)
            pathCounter+=1
        return stringList
    except:
        return 'Invalid Input: No such file or directory\n'

if __name__=='__main__':
    catReturn = cat(params=['bacon.txt','breakfast.txt'], path=['./','./'])
    for line in catReturn:
        sys.stdout.write(line)
    pass
