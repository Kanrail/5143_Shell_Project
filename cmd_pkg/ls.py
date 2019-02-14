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
            inf=str(inode.st_mode)
            #inf=str(stat.filemode(os.stat(files).st_mode)

            gid=str(g/home/sun/ls-l.pyetgrgid(inode.st_gid).gr_name)
            uid=str(getpwuid(inode.st_uid).pw_name)
            siz=str(inode.st_size)
            #time=str(inode.st_atime)
            date=datetime.utcfromtimestamp(inode.st_atime).strftime('%Y-%m-%d %H:%M:%S')
            #date=time.ctime(int(time))
            #date=datetime.datetime.fromtimestamp(int(time))
            permission ={'0':('---'),'1':('--x'),'2':('-w-'),'3':('-wx'),'4':('r--'),'5':('rw-'),'6':('rw-'),'7':('rwx')}
            #inf=str(permission(inode.st_mode))

            print(inf + ' ' + gid + ' ' + uid + ' '  + date +' '+ siz  + ' ' + name)

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
