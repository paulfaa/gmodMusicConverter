import os
import re
isTraitor = False

currentPath = os.getcwd()
folderPath = ""

try:
	with open (currentPath + "\sounds.txt", "r") as songFile:
		next(songFile) #skip header
		for line in songFile:
			matches = re.findall(r"""([^"]*)""", line)
			#print(matches)
			fileName = matches[2]
			artist = matches [6]
			track = matches [10]
			print(fileName + ", " + artist + ", " + track)
			if line[13] == "T":
				folderPath = "\\"+"traitor"+"\\"
			if line[13] == "I":
				folderPath = "\\"+"innocent"+"\\"
			else:
				folderPath = "\\"+"timeout"+"\\"
			print("Folderpath: " + currentPath + folderPath)
			try:
				with open(currentPath + folderPath + fileName, 'w') as outputFile:
					outputFile.write(track + '\n' + artist)
			except:
				print("Write file failed, check sounds.txt has no illegal characters")
except:
	print("Read file failed, check sounds.txt is in same directory as script")