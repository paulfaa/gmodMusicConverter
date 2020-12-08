import os
import re
import logging
import tkinter as tk
from tkinter import filedialog, Text

#Script to read the old 'sounds.txt' file from Garry's Mod round end plugin
#and create txt files for each mathcing the new format
#TODO: add GUI + function to generate txt files using id3 tags

def selectFile():
	try:
		fileName = filedialog.askopenfilename(initialdir="/", title = "Select sounds.txt",
		filetypes = (("Text File", "*.txt"),) )
		return fileName
	except:
		logging.exception("Failed to select file")
		
def createGUI():
	root = tk.Tk()
	canvas = tk.Canvas(root, height=200, width=300)
	canvas.pack()
	openFile = tk.Button(root, text="Convert file", padx=5, pady=5, command=convert)
	openFile.pack()

	root.mainloop()

def convert():
	folderPath = ""
	countFiles = 0
	fileToConvert = selectFile()
	currentPath = os.getcwd()
	try:
		with open (fileToConvert, "r") as songFile:
			next(songFile) #skip header
			for line in songFile:
				matches = re.findall(r"""([^"]*)""", line)
				fileName = matches[2]
				fileName = re.sub('.mp3$', '.txt', fileName)
				artist = matches [6]
				track = matches [10]
				if line[14] == "R":
					folderPath = "\\"+"traitor"+"\\"
				if line[14] == "N":
					folderPath = "\\"+"innocent"+"\\"
				if line[14] == "I":
					folderPath = "\\"+"timeout"+"\\"
				#print("Folderpath: " + currentPath + folderPath + fileName)
				fullPath = os.path.join(currentPath + folderPath)
				try:
					if not os.path.exists(fullPath):
						os.makedirs(fullPath)
					if not os.path.exists(fullPath + fileName):
						with open(fullPath + fileName, 'w') as outputFile:
							outputFile.write(track + '\n' + artist)
							countFiles = countFiles + 1
				except:
					logging.exception("Write file failed, check sounds.txt has no illegal characters")
		print("Script complete, created " + str(countFiles) + " files.")
	except:
		logging.exception("Read file failed, check sounds.txt is in same directory as script")
		
#selectFile()
createGUI()