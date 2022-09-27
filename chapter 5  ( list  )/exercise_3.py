
word=["abc","xyz"]

def rev_word(word) :
    rev=[]
    for i in word :
        rev.append(i[-1::-1])
    return rev

print(rev_word(word))