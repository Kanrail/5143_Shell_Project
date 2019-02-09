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
        cd changes the current working directory to PATH

    EXAMPLE
        cd /path/path2

    """
    if 'path' in kwargs:
        path = kwargs['path']

    try:
        '''if command ~ is given, it'll be subsituted by the shell with the user's
        home directory'''
        os.chdir(path[0])
        #print (os.getcwd()) #here for debugging purposes
    except:
        return 'Invalid Input: No such directory\n'

if __name__=='__main__':
    cd(path=['/'])
    pass
