import sys
import psutil
from datetime import datetime

def who (**kwargs):
    """
    WHO                         User Commands                        WHO
    NAME
        who - shows all users logged in
    SYNOPSIS
        who
    DESCRIPTION
        who displays a list of all users logged in as well as some information
        regarding their session

    EXAMPLE
        who
    """
    users = psutil.users()
    try:
        returnStrList = []
        for userObject in users:
            #userName, terminal, host, sessionStart = [suser for suser in userObject]
            userName = userObject.name
            terminal = userObject.terminal
            host = userObject.host
            if host == None: #if not the user is not remoted into the machine
                host = ''
            sessionStartTemp = int(userObject.started)
            sessionStart = datetime.utcfromtimestamp(sessionStartTemp).strftime('%b %d %H:%M')
            returnStrList.append(userName+' '+terminal+' '+host+' '+sessionStart+'\n')
        return returnStrList
    except:
        return 'Error: Something went wrong\n'

if __name__=='__main__':
    userList = who()
    for item in userList:
        sys.stdout.write(item)
    pass
