#!/usr/bin/env python
import threading
import sys
from cmd_pkg import commands


def exit(**kwargs):
    sys.exit()


class CommandHelper(object):
    def __init__(self):
        self.commands = {}
        self.commands['ls'] = ls
        self.commands['cat'] = cat
        self.commands['pwd'] = pwd
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


    def exists(self, cmd):
        return cmd in self.commands


if __name__ == '__main__':

    ch = CommandHelper()

    while True:
        # get input from terminal (use input if raw_input doesn't work)
        command_input = raw_input('% ')

        # remove command from params (very over simplified)
        command_input = command_input.split()

        # tags are any part of the command that star with a '-'
        for item in command_input:
            commandPiece = list(item)
            if

        # params are all but first position in list
        params = command_input[1:]

        # pull actual command from list
        cmd = command_input[0]

        # if command exists in our shell
        if ch.exists(cmd):
            ch.invoke(cmd=cmd, params=params,thread=True)
        else:
            print("Error: command %s doesn't exist." % (cmd))
