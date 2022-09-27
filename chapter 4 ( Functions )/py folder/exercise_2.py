

name =input("enter a word : ")

def is_palindrome(name) :
    name1=name[::-1]
    if name == name1 :
        return True
    
    return False

print(is_palindrome(name))