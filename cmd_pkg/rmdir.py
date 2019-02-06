import os
import sys

def rmdir (**kwargs):
    """
    RMDIR                         User Commands                        RMDIR
    NAME
        rmdir - deletes an empty directory
    SYNOPSIS
        rmdir [DIRECTORY...]
    DESCRIPTION
        rmdir deletes a DIRECTORY at location specified by the path preceding the
        wanted directory name. The directory must be empty or it will return an
        error

    EXAMPLE
        rmdir example_directory

    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']

    try:
        os.rmdir(path[0]+params[0])
        return ''
    except:
        return 'ERROR: Directory not empty or no such directory\n'
    #except: #want to expand upon this later, better error handling
        #return 'Invalid Input: No such file or directory\n'

if __name__=='__main__':
    sys.stdout.write(rmdir(params=['testdir2'],path=['./testdir/']))
    pass
