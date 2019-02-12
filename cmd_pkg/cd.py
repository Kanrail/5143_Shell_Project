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
    else:
        path = []
    if 'params' in kwargs:
        params = kwargs['params']
    else:
        params = []

    try:
        home = os.path.expanduser("~")
        print (path[0])
        if path ==[] and params ==[]:
            dirPath = home
        elif params != []:
            dirPath = path[0]+params[0]
        else:
            dirPath = path[0]

        if "~" in dirPath:
            dirPath = dirPath.replace("~", home)

        os.chdir(dirPath)
        #print ('Directory is now: '+os.getcwd()) #here for debugging purposes
        return ''
    except:
        return 'Invalid Input: No such directory\n'

if __name__=='__main__':
    sys.stdout.write(cd(path=["./"]))
    pass
