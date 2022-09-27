
# in with if 

name=input("enter your name :  ")
char=input("which character you search in name : ")

if char in name :
    print(f"{char} is presnt in{name}")
else :
    print("not present")