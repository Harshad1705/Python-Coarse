square={ 1:1 , 2:4 , 3:9}

square1={ i:i**2 for i in range(1,11)}
print(square1)

square3={f" square of {i}":i**2 for i in range(1,11)}
print(square3)

for k,v in square3.items() :
    print(f"{k}:{v}")

# create a dictionary to print no. of character in a string

s="harshad"
word_count={ char : s.count(char) for char in s }
print(word_count)