


age =int(input('enter your age : '))

if age==0 or age<0 :
    print("you cannot watch ")
elif 0<age<=10 :
    print('Ticket price : 100')
elif 10<age<=60 :
    print("Ticket price : 250" )
else :
    print("Ticket price : 200")