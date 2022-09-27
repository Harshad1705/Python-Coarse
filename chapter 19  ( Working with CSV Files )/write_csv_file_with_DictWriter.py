from csv import DictWriter 

with open("file3.csv","w",newline="") as f :
    csv_writer=DictWriter(f,fieldnames=["firstname","lastname","age"])
    csv_writer.writeheader()
    # methods - writerow , writerows
    # writerow({ key:value })
    csv_writer.writerow({
        "firstname":"harshad",
        "lastname":"lande",
        "age":18
    })
    csv_writer.writerow({
        "firstname":"kunal",
        "lastname":"lande",
        "age":12
    })
    # writerows([dict,dict,dict])
    csv_writer.writerows([
        {"firstname":"harshad","lastname":"lande","age":18} ,
        {"firstname":"kunal","lastname":"lande","age":12}
    ])