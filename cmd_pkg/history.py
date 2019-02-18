import sys
import os
from touch import touch

class History(object):
	"""
	Class name: History
	List of functions: __init__, historyIncIndex, historyDecIndex, getHistoryIndex, clearHistory
			   rebuildHistory, getHistoryFromIndex, getHistory
	Description: Interact with the many functions needed by the history class as it serves multiple
		roles within the shell program.
	"""
	def __init__(self):
		"""
		Name: __init__
		Input: None
		Output: None
		Description: Sets initial variables in use by the many other functions. Builds the initial
			history index based off existing ~/.history.txt file if it exists, if it doesn't, it
			creates it.
		"""
		self.currentIndex = 0
		self.fullHistory = []
		self.shellStorePath = os.path.expanduser("~")+'.shellhistory.txt'
		try:
			historyFile = open(self.shellStorePath)
			for line in historyFile:
				self.currentIndex+=1
				self.fullHistory.append(line)
		except:
			touch(path=[os.path.expanduser("~")],params=['.shellhistory.txt'])

	def historyIncIndex(self):
		"""
		Name: historyIncIndex
		Input: None
		Output: None
		Description: Increments the currentIndex variable. If index falls outside of current
			history list file, sets it to arbitrary value 999999999 to avoid out of bounds issues.
		"""
		self.currentIndex+=1
		if self.currentIndex > len(self.fullHistory)-1:
			self.currentIndex = 999999999


	def historyDecIndex(self):
		"""
		Name: historyDecIndex
		Input: None
		Output: None
		Description: Decrements the currentIndex variable. If index falls outside of current
			history list file, sets it to arbitrary value -1 to avoid out of bounds issues.
		"""
		if self.currentIndex == 999999999:
			self.currentIndex = len(self.fullHistory)-1
		else:
			self.currentIndex-=1
			if self.currentIndex < -1:
				self.currentIndex = -1

	def getHistoryIndex(self):
		"""
		Name: getHistoryIndex
		Input: None
		Output: currentIndex (int)
		Description: Returns the currentIndex value.
		"""
		return self.currentIndex

	def clearHistory(self):
		"""
		Name: clearHistory
		Input: None
		Output: None
		Description: Completely clears the ~/.history.txt file.
		"""
		historyFile = open(self.shellStorePath,'w').close()

	def rebuildHistory(self):
		"""
		Name: rebuildHistory
		Input: None
		Output: None
		Description: Rebuilds the fullHistory to update with any changes made to the
			~/.history.txt file.
		"""
		self.fullHistory = []
		historyFile = open(self.shellStorePath)
		for line in historyFile:
			self.currentIndex+=1
			self.fullHistory.append(line)

	def getHistoryFromIndex (self, index):
		"""
		Name: getHistoryFromIndex
		Input: index (int)
		Output: fullHistory[at index] (string)
		Description: Returns the string value at the index in fullHistory.
		"""
		return self.fullHistory[int(index)].strip('\n')

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
