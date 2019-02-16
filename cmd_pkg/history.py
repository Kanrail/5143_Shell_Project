import sys
import os
from touch import touch

class History(object):
	def __init__(self):
		self.currentIndex = -1
		self.fullHistory = []
		self.shellStorePath = os.path.expanduser("~")+'.shellhistory.txt'
		try:
			historyFile = open(self.shellStorePath)
			for line in historyFile:
				self.currentIndex+=1
				self.fullHistory.append(line.strip('\n'))
		except:
			touch(path=[os.path.expanduser("~")],params=['.shellhistory.txt'])

	def historyIncIndex(self):
		self.currentIndex+=1
		if self.currentIndex > len(self.fullHistory)-1:
			self.currentIndex = len(self.fullHistory)-1

	def historyDecIndex(self):
		self.currentIndex-=1
		if self.currentIndex < -1:
			self.currentIndex = -1

	def getHistoryIndex(self):
		return self.currentIndex

	def clearHistory(self):
		historyFile = open(self.shellStorePath,'w').close()

	def rebuildHistory(self):
		self.fullHistory = []
		historyFile = open(self.shellStorePath)
		for line in historyFile:
			self.currentIndex+=1
			self.fullHistory.append(line.strip('\n'))

	def getHistoryFromIndex (self, index):
		#if 'params' in kwargs:
		#	index = kwargs['params']
		#else:
			#return 'No parameter given, please try command again with a number following.\n'
		return self.fullHistory[int(index)]

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
		else:
			tags = []
		if 'params' in kwargs:
			command = kwargs['params']
		else:
			command = []

		if 'c' in tags:
			self.clearHistory()
			return
		elif command != []:
			with open(self.shellStorePath,'a') as historyFile:
				historyFile.write(command[0])
			self.rebuildHistory()
			self.currentIndex=len(self.fullHistory)-1
		else:
			returnStrList = []
			index = 0
			for item in self.fullHistory:
				returnStrList.append(str(index)+'  '+item)
				index+=1
			return returnStrList



if __name__=='__main__':
	HR = History()
	commandOutput = HR.getHistory()
	for line in commandOutput:
		sys.stdout.write(line)
	pass
