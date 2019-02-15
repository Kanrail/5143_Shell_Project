import os
import glob


import stat
from datetime import datetime
import time
from grp import getgrgid
from pwd import getpwuid


def lsn():
    try:
        path = glob.glob(os.path.join('*'))
        print(path)

    except:
        return 'Error\n'

def lsa():
    try:
        path = os.listdir(os.getcwd())
        print(path)

    except:
        return 'error\n'


def lsh():
    try:
        path = glob.glob(os.path.join('*'))
        path.sort(key=os.path.getsize)
        print(path)

    except:
        return 'error\n'


def lst():
    try:
        path = glob.glob(os.path.join('*'))
        path.sort(key=os.path.getmtime)
        print(path)

    except:
        return 'error\n'


def lsl():
    try:
        path  = os.listdir(os.getcwd())
        for name in path:
            files  = os.path.join(os.getcwd(), name)
            inode = os.stat(files)
            #inf=str(inode.st_mode)
            #inf=str(stat.filemode(os.stat(files).st_mode)

            gid=str(getgrgid(inode.st_gid).gr_name)
            #gid=str(inode.st_gid)
            #uid=str(inode.st_uid)
            uid=str(getpwuid(inode.st_uid).pw_name)
            siz=str(inode.st_size)

            b=''
            date=datetime.utcfromtimestamp(inode.st_atime).strftime('%Y-%m-%d %H:%M:%S')
            permission ={'8':'---','1':'--x','2':'-w-','3':'-wx','4':'r--','5':'rw-','6':'rw-','7':'rwx'}
            inf=str(inode.st_mode)
            for i in inf:
                b=b+permission[i]

            print(b + ' ' + gid + ' ' + uid + ' '  + date +' '+ siz  + ' ' + name)

    except:
        return 'error\n'


def ls(**kwargs):
    
    #if 'params' in kwargs:
     #   params=kwargs['params']
        
    if 'tags' in kwargs:
        tags=kwargs['tags']
        
    else:
        tags=[]
        
    #if 'path' in kwargs:
     #   path=kwargs['tags']
        
    try:
        returnString=''
        if not tags[0]:
            returnString = str(lsn())
        if 'a' in tags[0]:
            returnString = str(lsa())
        if 't' in tags[0]:
            returnString = str(lst())
        if 'h' in tags[0]:
            returnString = str(lsh())
        if 'l' in tags[0]:
            returnString = str(lsl())
            
        return returnString

    except:
        return 'error\n'

if __name__ == '__main__':
    print(ls(params=[''],tags=[''],path=['./']))

