import os
import stat
from datetime import datetime
import time
from grp import getgrgid
from pwd import getpwuid
def ls():
    try:
        path  = os.listdir(os.getcwd())
        for name in path:
            files  = os.path.join(os.getcwd(), name)
            inode = os.stat(files)
            inf=str(inode.st_mode)
            #inf=str(stat.filemode(os.stat(files).st_mode)
           
            gid=str(getgrgid(inode.st_gid).gr_name)
            uid=str(getpwuid(inode.st_uid).pw_name)
            siz=str(inode.st_size)
            time=str(inode.st_atime)
            #date=datetime.utcfromtimestamp(time).strftime('%Y-%m_d %H:%%M:%S')
            #date=time.ctime(int(time))
            #date=datetime.datetime.fromtimestamp(int(time))
            permission ={'0':('---'),'1':('--x'),'2':('-w-'),'3':('-wx'),'4':('r--'),'5':('rw-'),'7':('rwx')}
            #inf=str(permission(inode.st_mode))

            print(inf + ' ' + gid + ' ' + uid + ' '  + time +' '+ siz  + ' ' + name)

    except:
        return 'error\n'

if __name__ == '__main__':
    a=ls()
    print(a)
