
from csv import writer

with open("file2.csv","w",newline="") as f:
    csv_writer=writer(f)
    
    # methods - writerow , writerows

    csv_writer.writerow(["name","country"])
    csv_writer.writerow(["harshad","india"])
    csv_writer.writerow(["dale","south africa"])

    csv_writer.writerows([["AB","south africa"],["steve","australia"],["eoin","england"]])