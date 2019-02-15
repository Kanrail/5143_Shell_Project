#This is going to be the file where the commands are instantiated
from cat import cat
from cd import cd
from cp import cp
from grep import grep
from head import head
from ls import ls
from mkdir import mkdir
from mv import mv
from pwd2 import pwd
from rm import rm
from rmdir import rmdir
from sort import sort
from tail import tail
from wc import wc
from who import who
from touch import touch
from chmod import chmod

"""
This function iterates over globals.items() and if one of the values is "callable"
meaning it is a function, then I add it to a dictionary called 'invoke'. I also
add the functions '__doc__' string to a help dictionary.
Methods:
    exists (string) : checks if a command exists (dictionary points to the function)
    help (string) : returns the doc string for a function
"""
class CommandsHelper(object):
    def __init__(self):
        self.invoke = {}
        self.help = {}

        for key, value in globals().items():
            if key != 'Commands' and callable(value):
                self.invoke[key] = value
                self.help[key] = value.__doc__

    def exists(self,cmd):
        return cmd in self.invoke

    def help(self,cmd):
        return self.commands.invoke[cmd].__doc__



if __name__=='__main__':
    pass
