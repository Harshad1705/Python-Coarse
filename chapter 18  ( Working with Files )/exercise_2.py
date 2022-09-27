
with open("index.html","r") as webpage :
    with open('file3.txt',"w") as wf :
        for line in webpage.readlines() :
            if "<a href=" in line :
                pos =line.find("< href= ")
                first_quote= line.find('\"',pos)
                second_quote=line.find('\"',first_quote+1)
                url=line[first_quote+1:second_quote]
                wf.write(url+ "\n")