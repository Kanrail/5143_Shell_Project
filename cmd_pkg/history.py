import sys

def history (**kwargs):
    """
    HISTORY                         User Commands                        HISTORY
    NAME
        history - shows all previously entered commands
    SYNOPSIS
        history
	
	OPTIONS
		-c 		clears the command history
	
    DESCRIPTION
        history shows all previously entered commands in a sequential list with
		its index+1 to the left and the command to the right, 1 per line vertically.
    EXAMPLE
        history
    """
	if 'tags' in kwargs:
		tags = kwargs['tags']
	if 'command' in kwargs:
		command = kwargs['command']
	else:
		command = []
		
	historyList = []
	
	try:
		historyFile = open('.shellhistory.txt', 'a')
	except:
		historyFile = open('.shellhistory.txt','w+')
	
	if 'c' in tags:
		historyFile = open('.shellhistory.txt','w+')
		return
	elif command != []:
		historyFile.write(command, 'a')
	else:
		for line in historyFile:
			historyList.append(line)
		return historyList
