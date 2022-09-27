# with block / context manager 

with open ("file1.txt") as f:
    i=f.read()
    print(i)


print(f.closed)