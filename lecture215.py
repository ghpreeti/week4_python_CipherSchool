import pdb

# f = open("file1.txt")
# print(f"cursor position - {f.tell()}")
# print(f.read())
# print(f"cursor position - {f.tell()}")
# print("before seek method")
# f.seek(0)
# print("after seek method")
# print(f"cursor position - {f.tell()}")
# print(f.read())
# f.close()


# f = open("file1.txt")
# print(f"cursor position - {f.tell()}")
# print(f.readline(),end=" ")
# print(f.readline())
# print(f.readline())
# print(f"cursor position - {f.tell()}")
# print("before seek method")
# f.seek(0)
# print("after seek method")
# print(f"cursor position - {f.tell()}")
# print(f.read())
# f.close()


f = open("file1.txt")

lines = f.readlines()
print(len(lines))
for line in lines:
    print(line)

print(f.name)
print(f.closed)
# f.close()

for line in f:
    print(line)

f.close()

