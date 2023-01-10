import os
# os.getcwd()
os.chdir('')
print(os.getcwd())
os.mkdir('movies')
print(os.path.exists('movies'))
if os.path.exists('movies'):
    print('already exists')
else:
    os.mkdir('movies')  

open('file.txt','a').close()
os.mkdir(r'')

for item in os.listdir():
    D:#path address


for item in os.listdir():
    print(r'd\....\...\\...' + '\\' + item)

for item in os.listdir():
    path = os.pathjoin(os.getcwd(r'F:\path\address'),item)
    print(path)




