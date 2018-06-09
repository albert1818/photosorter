import os
import os.path

class MyFiles:

	def __init__(self, inputPath, outputPath):
		self.inputPath = inputPath
		self.outputPath = outputPath
		#self.nFiles = 0
	
	
#=== Methodes ==========================================================================================================
	
	# methode renames all directories in inputPath directory (no other subdirectories are renamed)
	# initial name hase to be in format: day.month.year
	# new name will be: year-mont-day
	def renameDirs(self):
		# print name of current directory
		print('Current directory: ' + os.path.basename(self.inputPath))
		
		# table with content of current directory
		content = os.listdir(self.inputPath)
		
		# if directory is not empty
		if content:
			# for each element in directory
			for piece in content:
				# if element is directory
				if os.path.isdir(self.inputPath + '/' + piece):
					# print its current name
					print(piece, end = '')
					
					# split the name where are dots (dmy - from: day.month.year)
					dmy = piece.split('.')
					
					# if dmy has 3 parts
					if len(dmy) == 3:
						# create new name in format y-m-d
						newName = dmy[2] + '-' + dmy[1] + '-' + dmy[0]
						
						# rename directory
						os.rename(self.inputPath + '/' + piece, self.inputPath + '/' + newName)
						
						# print new name
						print(" - new name: " + newName)
						
					# if dmy doesn't have 3 part, don't change the name
					else:
						print(" - not changed")
						
		# if directory is empty
		else:
			print('The directory is empty.')
	
	
	# methode sortFiles sorts files (copy) from inputPath into outputPath
	def sortFiles(self, dirLevel = 0):
		# print name of current directory with some space in fron to mark its level (dirLevel)
		print(dirLevel * "     " + os.path.basename(self.inputPath))
	
		# table with content of current directory
		content = os.listdir(self.inputPath)
	
		# if directory is not empty
		if content:
			dirLevel += 1
			
			# for each element in directory 
			for piece in content:
				# create new MyFiles object
				piecePath = MyFiles(self.inputPath + '/' + piece, self.outputPath)
			
				# if piecePath is directory
				if os.path.isdir(piecePath.inputPath):
					# recursion of sorting methode sortFiles
					piecePath.sortFiles(dirLevel)
				
				# if piecPath is file
				elif os.path.isfile(piecePath.inputPath):
					# print file name with extension
					print(dirLevel * "     " + os.path.split(piece)[1])
					
					# extension of the file
					fileExt = os.path.splitext(piecePath.inputPath)[1].lower()
					
					# if file is JPEG (if you want to change/add a type of sorted files,  
					# replace/add string defining the extension - eg. change '.jpe' to '.png')
					if ( fileExt == '.jpg' or fileExt == '.jpeg' or fileExt == '.jpe'):
						# what to do?
						print('---> JPEG!!!')
				
					# if file is not JPEG (or other defined before)
					else:
						# what to do?
						print(os.path.splitext(piecePath.inputPath)[1])
				
				# if piecPath is neither directory nor file
				else:
				# what to do?
					print(folderLevel * "     " + split(piece)[1])
		
		# if current directory is empty - return
		else:
			return