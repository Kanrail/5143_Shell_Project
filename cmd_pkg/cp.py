from shutil import copyfile
import sys

def cp (**kwargs):
    """
    CP                         User Commands                        CP
    NAME
        cp - copies
    SYNOPSIS
        cp [FILE...] [FILE2...]
    DESCRIPTION
        cp copies FILE to FILE 2.  FILE must be an existent file and if
        FILE2 already exists, the file will be overwritten with FILE.
        If no FILE and/or FILE2 is given,it will return an error.

    EXAMPLE
        cp file.txt file2.txt

    """
    if 'params' in kwargs:
        params = kwargs['params']

    try:
        copyfile(params[0],params[1])
        return ''
    except:
        return 'Invalid Input: No such file or directory'

if __name__=='__main__':
    sys.stdout.write(cp(params=['bacon.txt','bacon2.txt']))
    pass
