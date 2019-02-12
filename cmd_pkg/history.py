import sys

class History(object):
	def __init__(self):
		self.currentIndex = -1
		self.fullHistory = []
		try:
			historyFile = open('~/.shellhistory.txt')
			for line in historyFile:
				self.currentIndex+=1
				self.fullHistory.append(line)
		except:
			historyFile = open('~/.shellhistory.txt')

	def historyIncIndex(self):
		self.currentIndex+=1
		
	def historyDecIndex(self):
		self.currentIndex-1
		
	def getHistoryIndex(self):
		return self.currentIndex
		
	def clearHistory(self):
		historyFile = open('~/.shellhistory.txt','w+')
		
	def rebuildHistory(self):
		self.fullHistory = []
		historyFile = open('~/.shellhistory.txt')
		for line in historyFile:
			self.currentIndex+=1
			self.fullHistory.append(line)
		
	def getHistoryFromIndex (self, **kwargs):
		if 'params' in kwargs:
			index = kwargs['params]
		else:
			return 'No parameter given, please try command again with a number following.\n'
		return 
			self.fullHistory[index]

	def getHistory (self, **kwargs):
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
		if 'params' in params:
			command = kwargs['params']
		else:
			command = []
		
		historyFile = open('.shellhistory.txt','a')
		
		if 'c' in tags:
			self.clearHistory()
			return
		elif command != []:
			historyFile.write(command[0], 'a')
			self.historyIncIndex()
			self.rebuildHistory()
		else:
			return self.fullHistory
if __name__=='__main__':
    pass
