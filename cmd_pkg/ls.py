import sys
import os

def ls(**kwargs):
    """
    ls command is for listing all file's name in current location
    
    """
    if 'params' in kwargs:
        params = kwargs['params']
    if 'path' in kwargs:
        path = kwargs['path']
        
    output = os.listdir(path)
    if output == Null:
        print ("can't open direction")
        
    for params in output:
        print params