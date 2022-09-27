
number=[1,2,3,4,5]
print(max(number))
print(min(number))
print("\n")

def length (i) :
    return len(i)

name=["harshad","mohit","ab"]

print(max(name,key=length))
print(min(name,key=length))

print(max(name,key=lambda i :len(i)))
print(min(name,key=lambda i :len(i)))

print("\n\n")


student={
            "harshad" :{"score":90 , "age" :24} ,
            "mohit" : {"score":80 , "age":20} ,
            "rohit" : {"score":70 , "age":18}
}

print(max(student,key=lambda item : student[item]["score"]))
print(min(student,key=lambda item : student[item]["age"]))

print("\n")


student2=[
      {  "name"  :  "harshad" ,"score":90 , "age" :24 },
          { "name"  :  "mohit"  ,"score":80 , "age":20 },
           { "name"  : "rohit" ,"score":70 , "age":18}
]

print(max(student2,key=lambda i : i.get("score"))["name"])
print(min(student2,key=lambda i : i.get("age"))["name"])