import pdb  # import pdb module 
# module - python file contain usefull lasses and function wrote by developer 


# according to wikipedia - debugging is a process of finding and resolving defects or problems
#                         within a computer programm that prevent correct operation of
#                         computer software of a system 

# why debugging 
# 1. our programm is not running and causing unexpected errors
# 2. our program is running fine but not working the same way we want 

# steps for debugging
# 1. step trace
# 2. execute code line by line

pdb.set_trace()
name=input(" enter your name : ")
age=input(" enter your age : ")
print(f"Hello {name} your age is {age}")
age2=age+5
print(f"{name} you will be {age2} after 5 years ")