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
        Count lines, words and characters of a file and pass value back.

        -l  count number of lines in file
        -w  count number of words in file
        -m  count number of characters in file

    EXAMPLES
        wc file
            Output the number of lines, words, and characters back to function.
    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'flags' in kwargs:
        flags = kwargs['flags']
    else:
        flags = []

    try:
        iFile = params
        returnString = ''
        if not flags:
            return str(wcLines(iFile))+' '+str(wcWords(iFile))+' '+str(wcChars(iFile))+' '+params
        elif 'l' in flags:
            returnString = str(wcLines(iFile)) + ' '
        elif 'w' in flags:
            returnString = str(wcWords(iFile)) + ' '
        elif 'm' in flags:
            returnString = str(wcChars(iFile)) + ' '
        return returnString + params

    except:
        return 'Invalid Input: No such file or directory'

if __name__=='__main__':
    testData = {"params":'../bacon.txt'}
    print (wc(params='../bacon.txt'))
    pass
