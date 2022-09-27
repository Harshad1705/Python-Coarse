
name=input("enter your name : ")
# harshad
# name.count("h"),  name.count("name[0]") =2
# name.count("a"),  name.count("name[1]") =2
# name.count("r"),  name.count("name[2]") =1
# name.count("s"),  name.count("name[3]") =1
# name.count("h"),  name.count("name[4]") =h
# name.count("a"),  name.count("name[5]") =2
# name.count("d"),  name.count("name[6]") =1



temp_var=""
i=0

while i<len(name) :
    if name[i] not in temp_var :
        temp_var+=name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i+=1
