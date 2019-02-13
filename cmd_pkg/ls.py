import os
import glob

def ls-n(path):
    try:
        path = glob.glob(os.path.join('*'))
        print(path)

    except:
        return 'error\n'

def ls-a(path):
    try:
        path = os.listdir(os.getcwd())
        print(path)

    except:
        return 'error\n'

def ls-h(path):
    try:
        path = glob.glob(os.path.join('*'))
        path.sort(key=os.path.getsize)
        print(path)

    except:
        return 'error\n'

def ls-t(path):
    try:
        path = glob.glob(os.path.join('*'))
        path.sort(key=os.path.getmtime)
        print(path)

    except:
        return 'error\n'
def ls-l(path):
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

def ls():
    try:
        if not tags[0]:
            return str(ls-n(p))
        if 'a' in tags[0]:
            return str(ls-a(p))
        if 't' in tags[0]:
            return str(ls-t(p))
        if 'h' in tags[0]:
            return str(ls-h(p))
        if 'l' in tags[0]:
            return str(ls-l(p))

if __name__ == '__main__':
    a=ls()
    print(a)
