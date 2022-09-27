
input=["true","false",[1,2,3],1,1.0,3]


# def num_to_string(l) :
#     output=[]
#     for i in l :
#         if type(i)==int or type(i)==float :
#             output.append(str(i))
#     return output

# print(num_to_string(input))

output=[ str(i) for i in input if type(i)==int or type(i)==float]

print(output)