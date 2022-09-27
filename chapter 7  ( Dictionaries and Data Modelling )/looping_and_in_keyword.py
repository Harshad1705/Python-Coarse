
user_info={
    "name":"harshad" ,
    "age":18 ,
    "movie":"3 idiot"
}

# check key exist in dictionary

if "name" in user_info :
    print("present")
else :
    print("not present ")


if "name22" in user_info :
    print("present")
else :
    print("not present ")
     

print("\n\n")

# check if value present in dictionary

if "harshad" in user_info.values() :
    print('present')
else :
    print(" not present ")

print("\n\n")

# loop in dictionary

for i in user_info :
    print(i)                 # print all keys 

print('\n\n')

for i in user_info.values() :
    print(i)                 # print all values

print('\n\n')

# values method               # return list type of value

user_info_value=user_info.values()
print(user_info_value)                  
print(type(user_info_value))

print('\n\n')

# keys method                   # return list type of value

user_info_key=user_info.keys()
print(user_info_key)                  
print(type(user_info_key))

print('\n\n')

# print value with help of key

for i in user_info :
    print(user_info[i])

print('\n\n')

# items method                  # return a list in which tuples are present

user_info_item=user_info.items()
print(user_info_item)                  
print(type(user_info_item))

print("\n\n")

for key,value in user_info.items() :
    print(f"key is {key} and value is {value}")

print("\n\n")

for i in user_info.items() :
    print(i)