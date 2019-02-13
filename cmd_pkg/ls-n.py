import os
import glob

def ls():
    try:
        path = glob.glob(os.path.join('*'))
        print(path)

    except:
        return 'Error\n'
if __name__ == '__main__':
    a=ls()
    print(a)

