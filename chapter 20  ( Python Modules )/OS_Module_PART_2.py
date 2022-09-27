
import os
folederpath = input("Enter Folder Path : ")
os.chdir(r"D:\Python Note")

i=os.walk(folederpath)
for current_path,folder_names,file_names in i :
    print(f" current path : {current_path}")
    print(f" folder names : {folder_names}")
    print(f" files names : {file_names}")

# other usefull os module object and function 
#   and other usefull function of shutil module in copy