import os

def touch(**kwargs):
    """
    TOUCH                         User Commands                        TOUCH
    NAME
        touch - makes an empty file
    SYNOPSIS
        touch [FILE]
    DESCRIPTION
        touch makes a FILE at location specified by the path preceding the
        wanted file name, or in the current directory of no alternative
        path supplied

    EXAMPLE
        touch example.txt

    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']

    try:
        with open(path[0]+params[0], 'a'):
            os.utime(path[0]+params[0], None)
    except:
        return 'Invalid Input: No such directory'

if __name__=='__main__':
    touch(params=['test.txt'], path=['./'])
    pass
