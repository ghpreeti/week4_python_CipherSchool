# f = open("file1.txt")
# f.read()
# f.close()


# with block

with open("file1.txt") as f:
    data = f.read()
    print(data)

print(f.closed)    