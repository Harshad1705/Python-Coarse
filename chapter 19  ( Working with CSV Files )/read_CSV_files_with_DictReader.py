
from csv import DictReader 

with open("file.csv","r") as f :
    csv_reader=DictReader(f,delimiter=",")     # by default delimiter is comma 
    for i in csv_reader :
        print(i)
        print(i["name"])