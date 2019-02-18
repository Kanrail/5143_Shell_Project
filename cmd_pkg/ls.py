import os
import glob
import stat
from datetime import datetime
import time
from grp import getgrgid
from pwd import getpwuid
import itertools

def sliceReturn(n, iterable):
    """
    Name: sliceReturn
    Input: iterable
    Output: list of the iterable slice
    Description: Needed function for lsn for parsing columns.
    """
    return list(itertools.islice(iterable, n))

def lsn(**kwargs):
    """
    Name: lsn (ls normal)
    Input: params[aFlag (bool), hFlag (bool)]
    Output: returnStr (list of strings)
    Description: Is the ls command with no -l flag. Will output all files based upon whether
        the aFlag is True or not. aFlag will show all files including hidden, will only show
        non-hidden files if aFlag is False. Provides the data back in 5 columns alphabetically
        descending starting in column 1 through column 5.
    """
    if 'params' in kwargs:
        params = kwargs['params']
    else:
        params = [False,False]
    aFlag = params[0]
    hFlag = params[1]

    if aFlag == True:
        path = os.listdir(os.getcwd())
        path.insert(0, '..')
        path.insert(0, '.')
    elif hFlag == True: #actual -h tag doesn't do anything after testing if not also -l
        path = glob.glob(os.path.join('*'))
    else:
        path = glob.glob(os.path.join('*'))

    returnStr = []

    cCount = 5 #number of columns
    
    try: #handling edge case of not enough files
        columns, dangling = divmod(len(path), cCount)
        iterator = iter(path)
        columns = [sliceReturn(columns + (dangling > i), iterator) for i in range(cCount)]
        paddings = [max(map(len, column)) for column in columns]
        for row in itertools.izip_longest(*columns, fillvalue=''):
            returnStr.append('  '.join(file.ljust(pad) for file, pad in zip(row, paddings)))
    except:
        for item in path:
            returnStr.append(item)
    return returnStr

def humanReadNum(num):
    """
    Name: humanReadNum
    Input: num (int)
    Output: string 
    Description: Reads in a number in bytes, continues dividing it by 1024 until it can't without
        becoming fractional, and returns that value with associated letter to represent the category
        of datasize with it as a string.
    """
    for unit in ['B','K','M','G','T']:
        if num < 1024.0:
            if unit == 'B':
                numR = int(num)
            else:
                numR = '{:.{prec}f}'.format(num, prec=1)
            return "{}{}".format(numR,unit)
        num = num / 1024.0

def lsl(**kwargs):
    """
    Name: lsl
    Input: params[aFlag (bool), hFlag (bool)]
    Output: returnStr (list of strings)
    Description: Returns a list of strings with data in the following format. Also, the aFlag being True
        will list all files and directories, hidden and otherwise. The hFlag being True will change the bytes
        of the data to human readable with size suffixes.
        
        [permissions] [num of links to file] [user] [group] [size] [time of last modification]
    """
    if 'params' in kwargs:
        params = kwargs['params']
    else:
        params = [False,False]
    aFlag = params[0]
    hFlag = params[1]

    returnStrList = []

    path  = os.listdir(os.getcwd())
    for name in path:
        nameCheck = list(name)
        if nameCheck[0]=='.' and aFlag == False:#Will skip hidden files if a tag not present
            continue

        info = os.lstat(name)

        files  = os.path.join(os.getcwd(), name)
        inode = os.stat(files)

        isLink = os.path.islink(name)
        isDir = os.path.isdir(name)
        perms = ''

        if isLink:
            perms = 'l'
        if isDir:
            perms = 'd'
        else:
            perms = '-'

        permission ={
            '8':'---',
            '1':'--x',
            '2':'-w-',
            '3':'-wx',
            '4':'r--',
            '5':'rw-',
            '6':'rw-',
            '7':'rwx'
        }
        octalPerms = list(oct(info.st_mode)[-3:])

        for item in octalPerms:
            perms=perms+permission[item]

        nlink = info.st_nlink
        gid=str(getgrgid(inode.st_gid).gr_name)

        uid=str(getpwuid(inode.st_uid).pw_name)

        siz=info.st_size
        if hFlag == True:#Converts byte size to human readable if h tag present
            siz = humanReadNum(siz)

        date=datetime.utcfromtimestamp(info.st_mtime).strftime('%b %d %H:%M')


        returnStrList.append('{:10}'.format(perms)
                            +'{:4d}'.format(nlink)+' '
                            +'{:11}'.format(uid)
                            +'{:6}'.format(gid)
                            +'{:>6}'.format(siz)
                            +' '  + date
                            +' ' + name + '\n')
    return returnStrList

def ls(**kwargs):
    """
    LS                         User Commands                        LS
    NAME
        ls - lists files in current directory
    SYNOPSIS
        ls
    DESCRIPTION
        ls lists all non-hidden files in current directory
    OPTIONS
        -l long listing that details a number of attributes about the files
        -a lists all hidden files and directories in the current working directory
        -h changes the numerical byte output to human readable
    EXAMPLE
        ls
    """

    if 'tags' in kwargs:
        tags = kwargs['tags']
    else:
        tags=[]

    aFlag = False
    hFlag = False
    lFlag = False

    returnString=''
    if not tags:
        returnString = lsn()
    else:
        if 'a' in tags:
            aFlag = True
        if 'h' in tags:
            hFlag = True
        if 'l' in tags:
            lFlag = True
            returnString = lsl(params=[aFlag, hFlag])
        else:
            returnString = lsn(params=[aFlag, hFlag])

    return returnString

if __name__ == '__main__':
    lsReturn = ls(params=[''],tags=['a'],path=['./'])
    if type(lsReturn)==list :
        for line in lsReturn:
            print (line)
