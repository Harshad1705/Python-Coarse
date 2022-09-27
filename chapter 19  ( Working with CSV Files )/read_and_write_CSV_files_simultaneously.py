from csv import reader,writer

with open("file3.csv","r") as rf :
    with open("file4.csv","w",newline='') as wf :
        csv_reader=reader(rf)
        csv_writer=writer(wf)
        csv_writer.writerow(["first_name","last_name","age"])
        for row in csv_reader :
            csv_writer.writerow(row)