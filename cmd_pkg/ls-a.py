import os

def ls():
    try:
        path = os.listdir(os.getcwd())
        print(path)

    except:
        return 'error\n'

if __name__ == '__main__':
    a=ls()
    print(a)

