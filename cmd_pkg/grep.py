import sys

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
        if 'patterns' in kwargs:
            patterns = kwargs['patterns']
        if 'path' in kwargs:
            path = kwargs['path']

        try:
            inputFile = open(path[0]+params[0])
            retStringList = []
            for line in inputFile:
                if patterns in line:
                    retStringList.append(line)
            return retStringList
        except:
            return 'Invalid Input: No such file or directory'

if __name__=='__main__':
    grepReturn = grep(params=['bacon.txt'],patterns=['bacon'], path=['../'])
    for line in grepReturn:
        sys.stdout.write(line)
    pass
