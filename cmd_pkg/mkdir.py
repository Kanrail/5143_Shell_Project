import os
import sys

def mkdir (**kwargs):
    """
    MKDIR                         User Commands                        MKDIR
    NAME
        mkdir - makes a directory
    SYNOPSIS
        mkdir [DIRECTORY...]
    DESCRIPTION
        mkdir makes a DIRECTORY at location specified by the path preceding the
        wanted directory name, or in the current directory of no alternative
        path supplied

    EXAMPLE
        mkdir example_directory

    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']

    try:
        os.mkdir(path[0]+params[0])
        return ''
    except:
        return 'Invalid Input: No such file or directory'

if __name__=='__main__':
    sys.stdout.write(mkdir(params=['turkey'],path=['./testdir/']))
    pass
