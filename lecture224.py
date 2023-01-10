import pdb


# with open('love_story.txt','r',encoding 'utf-8') as f:
#     print(f.encoding)
#     data = f.read()
#     print(data)

with open("file1.txt",'r') as f:
    data = f.read(100)
    print(data)
    while len(data)>0:
        print(data)
        data = f.read(100)


