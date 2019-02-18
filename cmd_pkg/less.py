import curses
import pprint
import sys
import getch2

def less(**kwargs):
        """
        LESS                         User Commands                        LESS
        NAME
            less - displays a text that can be parsed through
        SYNOPSIS
            less [FILE]
        DESCRIPTION
            less displays FILE to console window overriding current console output
            FILE must exist, and can be navigating using page-up, page-down, arrow keys
            and can be exited with the esc key

        EXAMPLE
            less file.txt

        """
        if 'params' in kwargs:
            params = kwargs['params']
        if 'path' in kwargs:
            path = kwargs['path']

        #try:
        fileOpen = open(path[0]+params[0])
        counter = 0
        sys.stdout.write('\n')
        sys.stdout.write(params[0])
        sys.stdout.write('\n')
        for line in fileOpen:
            counter +=1
            if counter == 20:
                ch = getch2.Getch()
                while True:
                    char = list(ch.impl())
                    if char[0]=='\x1b':
                        char.append(ch.impl())
                        char.append(ch.impl())
                        if char[2] == 'B':
                            counter = 0
                            break
            sys.stdout.write(line)
        sys.stdout.write('END OF FILE\n')
        return ''
        #except:
            #return 'Invalid Input: No such file or directory\n'


        '''
        #Attempt to use curses to display to screen, will come back and try later

        pprint.pprint(mylines)
        #Start the curse display
        stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        stdscr.keypad(True)

        #Parameters for display
        begin_x = 20; begin_y = 7
        height = 5; width = 40
        win = curses.newwin(height,width,begin_y,begin_x)
        '''


        #End the curse display
        #curses.endwin()
if __name__=='__main__':
    print(less(params=['bacon.txt'], path=['./']))
    pass
