import os
import re
import logging
import mutagen
from mutagen.mp3 import EasyMP3 as MP3
import tkinter as tk
from tkinter import filedialog, Text

#Script to read the old 'sounds.txt' file from Garry's Mod round end plugin
#and create txt files for each mathcing the new format
#TODO: make GUI nicer and add function to generate txt files using id3 tags

label = ""
frame = ""
textBox = Text

def selectFile():
	try:
		fileName = filedialog.askopenfilename(initialdir="/", title = "Select sounds.txt",
		filetypes = (("Text File", "*.txt"),))
		return fileName
	except:
		logging.exception("Failed to select file")
		
def createGUI():
	root = tk.Tk()
	canvas = tk.Canvas(root, height=100, width=100)
	canvas.pack()
	textBox = Text(root)
	textBox.pack()
	openFile = tk.Button(root, text="Convert file", padx=5, pady=5, command=convert)
	openFile.pack()
	generateText = tk.Button(root, text="Generate txt files", padx=5, pady=5, command=generateTxt)
	generateText.pack()

	root.mainloop()

def printToGUI():
	hello = "hello"
	textBox.insert(1, hello)

def generateTxt():
	countFiles = 0
	folderPath = filedialog.askdirectory(initialdir="/", title = "Select folder to generate .txt files for")
	print(folderPath)
	for file in os.scandir(folderPath): 
		if file.name.endswith('.mp3'):
			id3 = MP3(file)
			if "title" in id3:
				title = id3["title"][0]
			else:
				title = "?"
			if "artist" in id3:
				artist = id3["artist"][0]
			else:
				artist = "?"
			print(artist + " " + title)
			txtFileName = re.sub('.mp3$', '.txt', file.name)
			if not os.path.exists(txtFileName):
				outputPath = os.path.join(folderPath + "/" + txtFileName)
				with open(outputPath, 'w') as outputFile:
					outputFile.write(artist + "\n" + title)
					outputFile.close()
					print("Created file")
					countFiles = countFiles + 1
	print("Script complete, created " + str(countFiles) + " files.")
	
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
							outputFile.close()
							countFiles = countFiles + 1
				except:
					logging.exception("Write file failed, check sounds.txt has no illegal characters")
		print("Script complete, created " + str(countFiles) + " files.")
	except:
		logging.exception("Read file failed, check sounds.txt is in same directory as script")
		
#selectFile()
createGUI()