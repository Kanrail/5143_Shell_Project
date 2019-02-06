import sys
from shutil import move

def mv(**kwargs):
    """
    MV                         User Commands                        MV
    NAME
        mv - moves or renames a file
    SYNOPSIS
        mv [FILE...] [FILE2...]
    DESCRIPTION
        mv renames and/or ovewrites FILE2 with FILE.  FILE must be an existent
        file and if FILE2 already exists, the file will be overwritten with FILE.
        If no FILE and/or FILE2 is given,it will return an error.

    EXAMPLE
        mv file.txt file2.txt

    """
    if 'params' in kwargs:
        params = kwargs['params']
    try:
        move(params[0],params[1])
        return ''
    except:
        return 'Invalid Input: No such file or directory\n'

if __name__=='__main__':
    sys.stdout.write(mv(params=['bacon.txt','bacon2.txt']))
    pass
