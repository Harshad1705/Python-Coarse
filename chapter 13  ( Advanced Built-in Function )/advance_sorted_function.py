
fruit=["grapes","mango","apple"]
fruit.sort()
print(fruit)

fruit2=("grapes","mango","apple")
new_fruit1=sorted(fruit2)
print(new_fruit1)

fruit3={"grapes","mango","apple"}
new_fruit2=sorted(fruit3)
print(new_fruit2)

guiters=[
    { "model":"pulsar" , "price":100000} ,
    { "model":"splender" , "price":45000} ,
    {"model" : "bullet" ,"price":150000}
]

print(sorted(guiters,key=lambda i:i["price"], reverse=True))

print(sorted(guiters,key=lambda i:i["price"]))