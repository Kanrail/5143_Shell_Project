import sys
import os
import pwd

def cd (**kwargs):
    """
    CD                         User Commands                        CD
    NAME
        cd - changes the working directory
    SYNOPSIS
        cd [PATH]
    DESCRIPTION
        cp changes the current working directory to PATH

    EXAMPLE
        cp /path/path2

    """
    if 'path' in kwargs:
        path = kwargs['path']

    try:
        os.chdir(path[0])
        #print (os.getcwd()) #here for debugging purposes
    except:
        return 'Invalid Input: No such directory\n'

if __name__=='__main__':
    cd(path=['./testdir'])
    pass
