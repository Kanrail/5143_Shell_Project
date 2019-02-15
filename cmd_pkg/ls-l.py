import os
import stat
from datetime import datetime
import time
from grp import getgrgid
from pwd import getpwuid
def ls():
    #try:
        path  = os.listdir(os.getcwd())
        for name in path:
            files  = os.path.join(os.getcwd(), name)
            inode = os.stat(files)
            #inf=str(inode.st_mode)
            #inf=str(stat.filemode(os.stat(files).st_mode)
                   
            gid=str(getgrgid(inode.st_gid).gr_name)
            uid=str(getpwuid(inode.st_uid).pw_name)
            siz=str(inode.st_size)
            
            b=''
            date=datetime.utcfromtimestamp(inode.st_atime).strftime('%Y-%m-%d %H:%M:%S')
            permission ={'8':'---','1':'--x','2':'-w-','3':'-wx','4':'r--','5':'rw-','6':'rw-','7':'rwx'}
            inf=str(inode.st_mode)
            for i in inf:
                b=b+permission[i]

            print(b + ' ' + gid + ' ' + uid + ' '  + date +' '+ siz  + ' ' + name)

    #except:
     #   return 'error\n'

if __name__ == '__main__':
    a=ls()
    print(a)
