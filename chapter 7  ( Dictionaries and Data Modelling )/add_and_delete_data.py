user_info={
    "name":"harshad" ,
    "age":18 ,
    "movie":"3 idiot"
}

# add data 

user_info["sport"]="cricket"
print(user_info)

print("\n\n")

# pop method                     // return type according to value in key:value pair

popped_item=user_info.pop("age")
print(f"you popped {popped_item} from dictionary")
print(user_info)

print("\n\n")

# popitem method                    //randomly delete key:value pair , return a tuple  

popped_item2=user_info.popitem()
print(f"ypu popped {popped_item2} from dictionary")
print(user_info)