# gmodMusicConverter for Round End Music plugin
Modules used: tkinter, mutagen
----------
Convert function: 

  used to convert obsolete Gmod sounds.txt into individual .txt files for the new version of the plugin
	
  File should be in a format like:
  
  -- Possibilities: INNOCENT, TRAITOR, TIMEOUT
	
  WST:AddSound(INNOCENT, "90s.mp3", "Artist", "Test")
	
  WST:AddSound(TRAITOR, "file.mp3", "Artist", "Sample")
  
	
----------
Generate function:

  Select a folder to generate .txt files for use with the plugin
  Data is pulled from the ID3 tags for each .mp3 file, these will display as '?' if no data is available
