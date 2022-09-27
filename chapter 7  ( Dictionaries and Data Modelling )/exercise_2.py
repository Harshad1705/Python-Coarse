
user={}

name=input(" enter your name : ")
age=int(input(" enter your age : "))

movie=input(" enter a movies seperated by comma ").split(",")
sport=input(" enter a sports seperated by comma ").split(",")

user["name"]=name
user["age"]=age
user["movie"]=movie
user["sport"]=sport

for key,value in user.items() :
    print(f"{key} : {value} ")
