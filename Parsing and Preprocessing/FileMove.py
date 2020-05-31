import shutil, os

# Global Variables for setting file paths
<<<<<<< HEAD
FILE_NAME_PATH = "C:\\Users\\VictorY\\Downloads\\movies_no_dir_ids.csv"
DESTINATION_PATH = "C:\\Users\\VictorY\\Desktop\\Missing_ID"
=======

FILE_NAME_PATH = "C:/Yuva/ITU/3rd Sem/Research Topics/Movies & Gender/Code/FileList.txt"
DESTINATION_PATH = "C:/Yuva/ITU/3rd Sem/Research Topics/Movies & Gender/Code/Dest"
>>>>>>> e6bc40affe28a3aa8f003c0c13bcbe90295f396b

#FILE_NAME = "C:\Yuva\ITU\3rd Sem\Research Topics\Movies & Gender\Code\FileList.txt"
#print(FILE_NAME.replace("\\", "/"))

with open(FILE_NAME_PATH, 'r') as file_handle:
    # convert file contents into a list
    files = file_handle.read().splitlines()

file_path = ['C:/Yuva/ITU/3rd Sem/Research Topics/Movies & Gender/Code/{0}'.format(i) for i in files]

print(file_path)

# Loop through and copy each file
<<<<<<< HEAD
for f in files:
     shutil.copy(f, DESTINATION_PATH)
=======
# for src in files:
#      shutil.copy(src, DESTINATION_PATH)
>>>>>>> e6bc40affe28a3aa8f003c0c13bcbe90295f396b
