# read file
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method

f=open("file1.txt","r")

print(f"Cursor position - {f.tell()}")
print(f.read())
print(f"Cursor position - {f.tell()}")
f.seek(0)
print(f"Cursor position - {f.tell()}")
print(f.read())
print(f"Cursor position - {f.tell()}")
f.close()

print("\n\n")

f=open("file1.txt","r")
print(f.readline())
print(f.readline(),end='')
print(f.readline(),end='')

print("\n\n")

f.seek(0)  
lines = f.readlines()
print(lines)
print(len(lines))
for i in lines :
    print(i,end='')

#  name , closed 

print("\n\n")
print(f.name)
print(f.closed)

print("\n\n")

for i in f :
    print(i,end='')

f.close()

print(f.closed)