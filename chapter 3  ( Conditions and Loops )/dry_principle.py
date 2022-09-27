import random
winning_number= random.randint(1,100)

guess=1                                        
number=int(input("ente a NUMBER : "))          
game_over= False


while not game_over :

    if winning_number==number :
        print("you WON , and you guessed in {} times".format(guess))
        game_over=True
    else : 
        if number < winning_number : 
            print(" too low")
           
        else : 
            print("too high ")
        
        guess+=1
        number=int(input("guess again : "))