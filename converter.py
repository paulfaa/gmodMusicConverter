import os
import re

currentPath = os.getcwd()
folderPath = ""

#Script to read the old 'sounds.txt' file from Garry's Mod round end plugin
#and create txt files for each mathcing the new format

def convert():
	try:
		with open (currentPath + "\sounds.txt", "r") as songFile:
			next(songFile) #skip header
			for line in songFile:
				matches = re.findall(r"""([^"]*)""", line)
				fileName = matches[2]
				fileName = re.sub('.mp3$', '.txt', fileName)
				print(fileName)
				artist = matches [6]
				track = matches [10]
				print(fileName + ", " + artist + ", " + track)
				#update this for TIMEOUT
				if line[13] == "T":
					folderPath = "\\"+"traitor"+"\\"
				if line[13] == "I":
					folderPath = "\\"+"innocent"+"\\"
				print("Folderpath: " + currentPath + folderPath + fileName)
				fullPath = os.path.join(currentPath + folderPath)
				print(fullPath)
				try:
					if not os.path.exists(fullPath):
						os.makedirs(fullPath)
					if not os.path.exists(fullPath + fileName):
						with open(fullPath + fileName, 'w') as outputFile:
							outputFile.write(track + '\n' + artist)
				except:
					print("Write file failed, check sounds.txt has no illegal characters")
	except:
		print("Read file failed, check sounds.txt is in same directory as script")
		
convert()