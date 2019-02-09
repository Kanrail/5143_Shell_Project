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
        dirPath = path[0]
        home = os.path.expanduser("~")
        if "~" in dirPath:
            dirPath = dirPath.replace("~", home)
        elif dirPath == "":
            dirPath = home

        os.chdir(dirPath)
        print ('Directory is now: '+os.getcwd()) #here for debugging purposes
        return ''
    except:
        return 'Invalid Input: No such directory\n'

if __name__=='__main__':
    sys.stdout.write(cd(path=["~/Projects"]))
    pass
