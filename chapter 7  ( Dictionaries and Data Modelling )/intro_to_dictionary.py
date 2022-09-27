
# dictionay also a data structure 

# Q -- why we use dictionary  
# A -- because of limitation of lists , list are not enought to represent real data

# example
user=["harshad",18,["3 idiot","avenger"],[" paagal","4 mendo"]]
# this list contain name , age , movie name and song name 
# you can do this but this is not a good way to do this

# Q -- what are dictionaries 
# A -- unordered collection of data in key : value pair

# How to create dictionary
user={"name" : "harshad" , "age" : 18}
print(user)
print(type(user))

# second way to create dictionary 
user1=dict( name='harshad' , age=18)
print(user1)

# how to access data from dictionary
# NOTE -- there is no indexing because of unordered collection of data 
print(user["name"])
print(user1["age"])

# which type of data a dictionary can store 
# anytype od data can be store in dictionary
# numbers , string , list , dictionary 
user2={
        "name":"amruta" ,
        "age":17 ,
        "fav_movie ":"note book" ,
        "fav_song":"......."
}

# user3 = {
#     user4 = {
#         "name":"amruta" ,
#      "age":17 ,
#      "fav_movie":"note book" , 
#      "fav_song":" Tera Chehra "
#     } , 
#     user1=user1=dict( name='harshad' , age=18)

# }

# how to add data in empty dictionary 
user_info={}
user_info["name"]="hasrshad"
user_info["age"]=18