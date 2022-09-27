while True :
    try :
        age=int(input(" Enter Age : "))  # seven # 7
    
    except ValueError :
        print("Please type integer")
    except :
        print(" Unexpected Error")
    else :
        print(f"user input {age}")
        break
    finally :
        print("finally blocks ....")