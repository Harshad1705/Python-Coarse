number=[1,5,3,9,8,7,5,4,6]

def is_even (a) :
    return a%2==0

evens=list(filter(is_even,number))
print(evens)


# By lambda expression

evens2=list(filter(lambda a:a%2==0,number))
print(evens2)

for i in evens :
    print(i)

# By list comprehension

nwe_evens=[ i for i in number if i%2==0]
print(nwe_evens)