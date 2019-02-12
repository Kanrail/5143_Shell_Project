import os
import glob

def ls():
    try:
        path = glob.glob(os.path.join('*'))
        path.sort(key=os.path.getsize)
        print(path)

    except:
        return 'error\n'


if __name__ == '__main__':
    a=ls()
    print(a)
