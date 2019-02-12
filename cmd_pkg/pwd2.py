import sys
import os

def pwd (**kwargs):
    """
    PWD                         User Commands                        PWD
    NAME
        pwd - prints the current working directory
    SYNOPSIS
        pwd
    DESCRIPTION
        cp prints the current working directory

    EXAMPLE
        pwd

    """
    return [str(os.getcwd())]

if __name__=='__main__':
    returnCwd = pwd()
    sys.stdout.write(returnCwd[0]+'\n')
    pass
