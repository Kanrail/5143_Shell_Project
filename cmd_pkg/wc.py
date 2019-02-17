def wcLines (inputFile):
    iFile = open(inputFile)
    lineCount = 0
    for line in iFile:
        lineCount+=1
    return lineCount

def wcWords (inputFile):
    iFile = open(inputFile)
    wordCount = 0
    for line in iFile:
        lineWords = line.split()
        wordCount+=len(lineWords)
    return wordCount

def wcChars (inputFile):
    iFile = open(inputFile)
    return len(iFile.read())


def wc(**kwargs):
    """
    NAME
        wc - line count, wordcount, and character count of file and
        pass those values back to calling function.
    SYNOPSIS
        wc [OPTION]... [FILE]...
    DESCRIPTION
        wc count lines, words and characters, or specific sets of those as
        specified by OPTIONS of FILE and passes a string back containing that
        info.
        If no FILE is given, it will return an error.

    OPTIONS
        -l  count number of lines in file
        -w  count number of words in file
        -m  count number of characters in file

    EXAMPLES
        wc file
            Output the number of lines, words, and characters back to function.
        wc bacon.txt
            81 680 4748 ../bacon.txt
    """
    iFile = ''
    if 'params' in kwargs:
        params = kwargs['params']
    if 'tags' in kwargs:
        tags = kwargs['tags']
    else:
        tags = []
    if 'path' in kwargs:
        path = kwargs['path']
        iFile = path[0]+params[0]
    else:
        iFile = params[0]
    try:
        print(iFile)
        returnString = ''
        if not tags:
            return str(wcLines(iFile))+' '+str(wcWords(iFile))+' '+str(wcChars(iFile))+' '+params[0]
        if 'l' in tags[0]:
            returnString += str(wcLines(iFile)) + ' '
        if 'w' in tags[0]:
            returnString += str(wcWords(iFile)) + ' '
        if 'm' in tags[0]:
            returnString += str(wcChars(iFile)) + ' '
        return [returnString + params[0]]

    except:
        return 'Invalid Input: No such file or directory'

if __name__=='__main__':
    print (wc(params=['/Users/hellspawn/Projects/5143_Shell_Project/bacon.txt'], tags=[''], path=['']))
    pass
