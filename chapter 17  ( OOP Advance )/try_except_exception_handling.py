
while True :
    try :
        age=int(input(" Enter Age : "))  # seven # 7
        break 
    except ValueError :
        print(" You entered wrong input")
    except :
        print(" Unexpected Error")

if age<18 :
    print(" you can't play")
else :
    print(" you can play")