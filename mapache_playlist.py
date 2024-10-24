'''

Create folder containing <song_cnt> random .mp3, .m4a files

'''

import math
import os
import random
import shutil

src = os.walk("d:\music\\")
dest = "d:\\tmp"
keyword1 = ".mp3"
keyword2 = ".m4a"

def searchFiles(keyword1, keyword2) :
# {
	found = []
	
	for path, dirs, files in src :
	# {		
		for file in files :
		# {
			file = file.lower()

			if (file.find(keyword1) > -1 or file.find(keyword2) > -1) :
			# {
				found.append(path + "\\" + file)
			# }
			
			else :
			# {
				None
			# }

		# }

	return found

    # }

# }
	
songs = searchFiles(keyword1, keyword2)
song_cnt = input("How many songs? ")
tmp = -1

for i in range(int(song_cnt)) :
# {
	try :
	# {
		tmp = songs[math.floor(random.random() * len(songs))]
		shutil.copy(tmp, dest)
		print(tmp, dest)
	# }

	except :
	# {
		None
	# }
# }

'''

********
BONEYARD
********

# cnt = 1
			# cnt = cnt + 1
				

dirs

import glob
import sys

# print(math.floor(random.random() * len(songs)))
# print(songs[math.floor(random.random() * len(songs))])

# Destination path
destination = "/home/User/Documents/file.txt"
 
# Copy the content of
# source to destination
 
try:
    shutil.copy(source, destination)
    print("File copied successfully.")
 
# If source and destination are same
except shutil.SameFileError:
    print("Source and destination represents the same file.")
 
# If there is any permission issue
except PermissionError:
    print("Permission denied.")
 
# For other errors
except:
    print("Error occurred while copying file.")

# print(song_cnt, len(items))

# totalFiles = len(files)

# print("Starting Search...")

# print(str(cnt) + " of " + str(totalFiles) + " - " + file, end = "\r")

# os.system("cls")	# clear screen

# title =  "Found " + str(len(items)) + " items"

# print(title)
# print("-" * len(title))

# for item in items :
# {
#	print(item)
# }

# location = os.walk(sys.argv[1])
# keyword = sys.argv[2].lower()
# location = "d:\music"
# print(path, dirs, files)

'''