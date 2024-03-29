#!/usr/bin/env python
import threading
import sys, tty, termios
import os
from cmd_pkg import commands
import getpass
from cmd_pkg import history
import readline
import getch2


def exit(**kwargs):
    """
    Function Name: exit
    Input: None
    Output: None
    Description: Exits the shell program.
    """
    sys.exit()


class CommandHelper(object):
    """
    Class Name: CommandHelper 
    Functions: __init__, getThread, invoke, exists,printCmdOutput, readInput
    Description: Contains all functions to reading in, printing, and utilizing the commands
    """
    def __init__(self):
        """
        Method Name: __init__
        Input: None
        Output: None
        Description: Construsts the initial commands dictionary as well as setting up the threads pool
            variables
        """
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
        self.commands['touch'] = commands.touch
        self.commands['chmod'] = commands.chmod
        self.commands['less'] = commands.less
        self.commands['exit'] = exit
        self.tCounter = -1
        self.tPool = []

    def getThread(self,dFlag):
        """
        Method Name: getThread
        Input: dFlag (bool)
        Output: a list with tType(string), tName(string), and empty string
        Description: Increments tCounter for a new unique thread to be in tPool (thread pool)
        and marks whether that thread is a daemon or nondaemon.
        """
        tType = ''
        tName = ''
        self.tCounter+=1
        if dFlag==True:
            tType = 'daemon'
        else:
            tType = 'non-daemon'
        tName = 'thread'+str(self.tCounter)
        return [tType,tName,' ']

    def invoke(self, **kwargs):
        """
        Method Name: invoke
        Input: cmd (string), params(list of strings), thread (bool), tags (list of chars), path (list of strings)
        Output: Returns whatever data comes back from the command being called (string or list of strings)
        Description: Sets up the commands call
        """
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
            thread = (False,False)

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
        if thread[1]==False:
            print('NOT FIRING AS THREAD')
            return self.commands[cmd](params=params, path=path, tags=tags)
        else:
            print('STARTING THREAD')
            self.tPool.append(self.getThread(thread[0]))
            # Using a thread ****** broken right now *********
            if len(params)+len(tags)+len(path) > 0:
                self.tPool[self.tCounter][2] = threading.Thread(name=str(self.tPool[self.tCounter][1]),
                                                            target=self.commands[cmd],
                                                            args=**kwargs)
            else:
                self.tPool[self.tCounter][2] = threading.Thread(name=str(self.tPool[self.tCounter][1]),
                                                            target=self.commands[cmd])
            if self.tPool[self.tCounter][0] =='daemon':
                self.tPool[self.tCounter][2].setDaemon(True)

            self.tPool[self.tCounter][2].start()
            print('FIRING')
            return self.tPool[self.tCounter][2].join()
       '''

    def exists(self, cmd):
        """
        Method Name: exists
        Input: cmd (string)
        Output: bool
        Description: Returns True if command is in commands, else returns false
        """
        return cmd in self.commands

    def printCmdOutput(self, output, **kwargs):
        """
        Method Name: printFile
        Input: output(list of str or str), printParams(outputToCmd(bool),outputToFile(bool),appendToFile(bool))
        Output: Prints to screen or file depending on printParams passed in
        Description: Prints to screen or file depending on printParams passed in.
        """
        printFile = ''
        if 'printParams' in kwargs:
            printParams = kwargs['printParams']
            try:
                if printParams[1]==True:
                    printFile = open(printParams[3],'w')
            except:
                sys.stdout.write('Error: Invalid file or path given.\n')
                return
        else:
            printParams = [True,False,False,''] #print to CMD,print to file,append to file,printing file

        if type(output) is list:
            for line in output:
                if printParams[0]==True:
                    sys.stdout.write(line.strip('\n') + '\n')
                elif printParams[1]==True:
                    printFile.write(line.strip('\n')  + '\n')
                else:
                    with open(printParams[3],'a') as pFile:
                        pFile.write(line.strip('\n')  + '\n')
        elif type(output) is str:
            if printParams[0]==True:
                sys.stdout.write(output.strip('\n')  + '\n')
            else:
                printFile.write(output.strip('\n')  + '\n')
        else:
            pass

    def readInput(self,**kwargs):
        """
        Method Name: readInput
        Input: params (2 strings)
        Output: input (string)
        Description: Using Getch will handle character input to either parse through history for a
            command using up and down arrow keys, or user can input their own command. Upon pressing
            enter the command will be returned as a completed string.
        """
        hist = history.History()
        cursorIndex = 0
        ch = getch2.Getch()

        if 'params' in kwargs:
            params = kwargs['params']

        prompt = params[0]+' '+params[1]+'% '

        input = ''
        while (True):
            sys.stdout.write('\r'+'                                            '
                                 +'     ')
            sys.stdout.write('\r'+prompt+input)
            char = list(ch.impl())
            currentIndex = hist.getHistoryIndex()
            #print (char)
            if char[0]=='\x1b':
                char.append(ch.impl())
                char.append(ch.impl())
                if char[2] == 'A':
                    #input = 'UP ARROW'
                    hist.historyDecIndex()
                    currentIndex = hist.getHistoryIndex()
                    if currentIndex == -1:
                        input = hist.getHistoryFromIndex(0)
                    else:
                        input = hist.getHistoryFromIndex(currentIndex)

                elif char[2] == 'B':
                    #input = 'DOWN ARROW'
                    hist.historyIncIndex()
                    currentIndex = hist.getHistoryIndex()
                    if currentIndex==999999999:
                        input = ''
                    else:
                        input = hist.getHistoryFromIndex(currentIndex)
            elif char[0]=='\x7f':
                try:
                    input = input[:-1]
                    sys.stdout.write('\b ')
                    sys.stdout.flush()
                except:
                    input = ''
            elif char[0]=='\r':
                sys.stdout.write('\n')
                break

            else:
                input= input+char[0]
                pass
            sys.stdout.write('\r'+'                                            '
                                 +'    ')
            sys.stdout.write('\r'+prompt+input)
            sys.stdout.flush()
        return input

def pathParse(paramList):
    """
    Function Name: pathParse
    Input: paramList (contains strings)
    Output: string(joined path list), pathEnd (int)
    Description: Parses a path given counting the slashes and returns the path
        minus the filename with a char index(pathEnd) denoting the end of the path
    """
    paramPath = []
    pathEnd = 0
    charCounter = 0
    for char in paramList:
        if char == '/':
            pathEnd = charCounter
        charCounter+=1

    return [''.join(paramList[0:pathEnd+1]), pathEnd]


if __name__ == '__main__':

    ch = CommandHelper()
    hist = history.History()

    pipeOutput = os.path.expanduser("~")+'/.temp.txt'

    while True:

        # get input from terminal (use input if raw_input doesn't work)
        currentDirectory = os.path.basename(os.getcwd())
        currentUser = getpass.getuser()
        command_input = ch.readInput(params=[currentDirectory, currentUser])
        #Add the command to the history file
        hist.getHistory(params=[command_input+'\n'])

        # remove command from params (very over simplified)
        command_input = command_input.split()

        # reset loop variables
        brokenCommand = False
        outputToCmd = True
        outputToFile = False
        appendToFile = False
        printFile = ''

        # tags are any part of the command that start with a '-'
        tags = []
        path = []

        #if user is pulling a command back
        tempCmdList = list(command_input[0])
        if tempCmdList[0] == '!':
            try:
                prevCommandIndex = int(''.join(tempCmdList[1:]))
                command_input = hist.getHistoryFromIndex(prevCommandIndex)
                sys.stdout.write(command_input+'\n')
                command_input = command_input.split()
                tempCmdList = list(command_input[0])
            except:
                sys.stdout.write('Invalid parameter.\n')
                continue

        for item in command_input[1:]:#Parses the command parameters and tags
            commandPiece = list(item)
            if commandPiece[0]=='-':#If the parameter is a tag
                commandPiece.remove('-') 
                if 'n' in commandPiece: #special case n to ensure integer follows the n tag
                    tags.append('n')
                    hasNumber = False
                    wholeTagLine = ''.join(commandPiece)
                    nextCommand = command_input[command_input.index(item)+1]
                    for char in wholeTagLine: #reads in that value if its a number, then stops processing that param
                        if char.isdigit(): #if the value for -n is attached without a space
                            tags.append(''.join(num for num in wholeTagLine if num.isdigit()))
                            break
                else:
                    for tag in commandPiece:
                        tags.append(tag)
                command_input.remove(item)
            elif command_input[command_input.index(item)]=='>':#output to a file
                outputToCmd = False
                outputToFile = True
                command_input.pop(command_input.index(item))
                printFile = command_input.pop()
                break
            elif command_input[command_input.index(item)]=='>>':#append to a file
                outputToCmd = False
                appendToFile = True
                command_input.pop(command_input.index(item))
                printFile = command_input.pop()
                break
            elif command_input[command_input.index(item)]=='|':#feed output from previous command into next
                outputToCmd = False
                outputToFile = True
                printParams = [outputToCmd,outputToFile,appendToFile,pipeOutput]
                if ch.exists(command_input[0]):
                    ch.printCmdOutput(ch.invoke(cmd=command_input[0],
                                                tags=tags,
                                                path=path,
                                                params=command_input[1:command_input.index(item)],
                                                thread=True)
                                                ,printParams=printParams)
                elif cmd == 'history':
                    ch.printCmdOutput(hist.getHistory(tags=tags), printParams=printParams)
                else:
                    print("Error: command %s doesn't exist." % (command_input[0]))
                    brokenCommand = True
                    break
                #Reset most of the command variables for the following commands
                tags = []
                path = []
                params = []
                outputToCmd = True
                outputToFile = False
                pipeIndex = command_input.index(item)
                command_input = command_input[pipeIndex+1:]
                command_input.insert(1, pipeOutput)
                pipePiece = list(pipeOutput)
                pathP = pathParse(pipePiece)
                path.append(pathP[0])
                #removes the path from the parameter
                command_input[1]=''.join(pipePiece[pathP[1]+1:])
            elif '/' in commandPiece: #indicating that there may be a lengthy path
                pathP = pathParse(commandPiece)
                path.append(pathP[0])
                #removes the path from the parameter
                command_input[command_input.index(item)]=''.join(commandPiece[pathP[1]+1:])
            elif item== '..':#backup one directory
                path.append(item)
                command_input.pop(command_input.index(item))
            elif item== '~':#home path
                path.append(item)
                command_input.pop(command_input.index(item))
            else: # path for every parameter, if none given will insert just a ./
                path.append(str(os.getcwd())+'/')

        if brokenCommand == True:#command before pipe invalid command, start new line
            continue

        #printing paramaters
        printParams = [outputToCmd,outputToFile,appendToFile,printFile]
        # params are all but first position in list
        params = command_input[1:]

        # pull actual command from list
        cmd = command_input[0]

        #if command is history

        # if command exists in our shell
        if ch.exists(cmd):
            ch.printCmdOutput(ch.invoke(cmd=cmd,tags=tags,path=path,params=params,thread=(False,True))
                                        ,printParams=printParams)

        elif cmd == 'history':
            ch.printCmdOutput(hist.getHistory(tags=tags), printParams=printParams)

        else:
            print("Error: command %s doesn't exist." % (cmd))
