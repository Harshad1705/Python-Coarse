
with open("file1.txt","r") as rf :
    with open("file2.txt","w") as wf :
        for i in rf :
            name,salary=i.split(",")
            wf.write(f"{name}'s salary is {salary}")