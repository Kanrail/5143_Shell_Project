import os


def ls():
    try:
        path  = os.listdir(os.getcwd())
        for name in path:
            files  = os.path.join(os.getcwd(), name)
            inode = os.stat(files)
            print(str(inode.st_gid) + ' '  + str(inode.st_uid) + ' ' + str(inode.st_size) + ' ' +  str(inode.st_atime) + ' ' + name)

    except:
        return 'error\n'

if __name__ == '__main__':
    a=ls()
    print(a)
