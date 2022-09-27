import os

print(os.getcwd())

os.chdir(r"D:\Python Note\Practise Programm")

if os.path.exists("chapter 20  ( Python Modules )") :
    print(" already exist")
else:
    os.mkdir("chapter 20  ( Python Modules )")

print(os.listdir())

print(os.listdir('E:'))

for item in os.listdir() :
    i=os.path.join(os.getcwd(),item)
    print(i)