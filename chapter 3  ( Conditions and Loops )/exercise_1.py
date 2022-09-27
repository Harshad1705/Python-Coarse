winning_number=17

gusee_number=int(input("enter any number betweer 1 to 25 : "))

if winning_number==gusee_number :
    print("YOU WON")
else :
    if winning_number>gusee_number :
        print("you gussed low number")
    else :
        print("you gussed high number")
