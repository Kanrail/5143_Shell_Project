import os
import stat
import datetime
def ls():
    try:
        path  = os.listdir(os.getcwd())
        for name in path:
            files  = os.path.join(os.getcwd(), name)
            inode = os.stat(files)
            #inf=str(inode.st_mode)
            #inf=str(stat.filemode(os.stat(files).st_mode))
            inf=str(inode.st_mode)
            gid=str(inode.st_gid)
            uid=str(inode.st_uid)
            siz=str(inode.st_size)
            time=str(inode.st_atime)
            #date=datetime.datetime.fromtimestamp(time)
            print(inf + ' ' + gid + ' ' + uid + ' '  + time +' '+ siz  + ' ' + name)

    except:
        return 'error\n'

if __name__ == '__main__':
    a=ls()
    print(a)
