#!/usr/bin/env python
import threading
import sys
import os
from cmd_pkg import commands
import getpass


def exit(**kwargs):
    sys.exit()


class CommandHelper(object):
    def __init__(self):
        self.commands = {}
        self.commands['ls'] = commands.ls
        self.commands['cat'] = commands.cat
        self.commands['pwd'] = commands.pwd
        self.commands['cd'] = commands.cd
        self.commands['cp'] = commands.cp
        self.commands['grep'] = commands.grep
        self.commands['head'] = commands.head
        self.commands['mkdir'] = commands.mkdir
        self.commands['mv'] = commands.mv
        self.commands['rm'] = commands.rm
        self.commands['rmdir'] = commands.rmdir
        self.commands['tail'] = commands.tail
        self.commands['wc'] = commands.wc
        self.commands['who'] = commands.who
        self.commands['sort'] = commands.sort
        self.commands['exit'] = exit

    def invoke(self, **kwargs):
        if 'cmd' in kwargs:
            cmd = kwargs['cmd']
        else:
            cmd = ''

        if 'params' in kwargs:
            params = kwargs['params']
        else:
            params = []

        if 'thread' in kwargs:
            thread = kwargs['thread']
        else:
            thread = False

        if 'tags' in kwargs:
            tags = kwargs['tags']
        else:
            tags = []

        if 'path' in kwargs:
            path = kwargs['path']
        else:
            path = []
        return self.commands[cmd](params=params,path=path,tags=tags)
        '''
        # One way to invoke using dictionary
        if not thread:
            self.commands[cmd](params=params)
        else:
            # Using a thread ****** broken right now *********
            if len(params) > 0:
                c = threading.Thread(target=self.commands[cmd], args=tuple(kwargs))
            else:
                c = threading.Thread(target=self.commands[cmd])

            c.start()
            c.join()
        '''

    def exists(self, cmd):
        return cmd in self.commands


if __name__ == '__main__':

    ch = CommandHelper()

    while True:
        # get input from terminal (use input if raw_input doesn't work)
        currentDirectory = os.path.basename(os.getcwd())
        currentUser = getpass.getuser()
        command_input = raw_input(currentDirectory+' '+currentUser+'% ')

        # remove command from params (very over simplified)
        command_input = command_input.split()

        # tags are any part of the command that start with a '-'
        tags = []
        path = []
        for item in command_input[1:]:
            commandPiece = list(item)
            if commandPiece[0]=='-':
                commandPiece.remove('-')
                if 'n' in commandPiece:
                    tags.append('n')
                    hasNumber = False
                    wholeTagLine = ''.join(commandPiece)
                    nextCommand = command_input[command_input.index(item)+1]
                    for char in wholeTagLine:
                        if char.isdigit(): #if the value for -n is attached without a space
                            tags.append(''.join(num for num in wholeTagLine if num.isdigit()))
                            break
                        '''elif nextCommand.isdigit(): #if there is a space between -n and its value
                            tags.append(nextCommand)
                            command_input.remove(nextCommand)
                            break'''
                else:
                    for tag in commandPiece:
                        tags.append(tag)
                command_input.remove(item)
            elif '/' in commandPiece:
                paramPath = []
                pathEnd = 0
                for char in commandPiece:
                    if char == '/':
                        pathEnd = commandPiece.index(char)
                path.append(''.join(commandPiece[0:pathEnd]))
                #removes the path from the parameter
                command_input[command_input.index(item)]=''.join(commandPiece[pathEnd+1:])
            elif item== '..':
                path.append(item)
                command_input.pop(command_input.index(item))
            elif item== '~':
                path.append(item)
                command_input.pop(command_input.index(item))
            elif command_input.index(item)=='|':
                #Do nothing for now, will get this working later. Ignoring further commands for now
                command_input = command_input[0:command_input.index(item)-1]
            else: #if a paremeter has no path given, default a paremeter of local
                path.append('./')

        # path for every parameter, if none given will insert just a ./

        # params are all but first position in list
        params = command_input[1:]

        # pull actual command from list
        cmd = command_input[0]

        # if command exists in our shell
        if ch.exists(cmd):
            #print ('Command is '+str(cmd))
            #print ('Tags are '+str(tags))
            #print ('Paths are '+str(path))
            #print ('Params are '+str(params))
            returnStatement = ch.invoke(cmd=cmd,tags=tags,path=path,params=params,thread=True)
            #if cmd == 'cd':
                #print ('Directory is now: '+os.getcwd())
            if type(returnStatement) is list:
                for line in returnStatement:
                    sys.stdout.write(line)
                sys.stdout.write('\n')
            elif type(returnStatement) is str:
                sys.stdout.write(returnStatement+'\n')
            else:
                pass
        else:
            print("Error: command %s doesn't exist." % (cmd))
