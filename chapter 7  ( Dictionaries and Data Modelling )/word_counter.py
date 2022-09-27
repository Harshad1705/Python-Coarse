

def word_count(s) :
    count={}
    for i in s :
        count[i]=s.count(i)
    return count

print(word_count("harshad"))