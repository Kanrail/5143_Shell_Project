from cmd_pkg import commands_test
#from cmd_pk import commands
import threading
import sys

def run_command(cmd, args=None,flags=None)
    if args:
        c = threading.Thread(target=cmd, args=(args,))
    else:
        c = threading.Thread(target=cmd)

    c.start()
    c.join()
