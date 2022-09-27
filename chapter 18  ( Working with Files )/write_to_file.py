
# w , a , r+

# w  - used to write content in file 
#      if file not exist then it create a new file
#      it delete all content and write from starting

#  a  - used to write content in file 
#      if file not exist then it create a new file
#      not delete the content of file and write after content of file

# r+ - used to write and read in file
#       it did not create new file 
#       write the content from starting and over-write on before content

with open("file1.txt" , "w") as f :
    f.write("Hello ")

with open("file1.txt" , "a") as f :
    f.write(' please do it')

with open("file1.txt" , "r+") as f :
    f.seek(len(f.read()))
    f.write("you can do this ")
    print(f.read())