import os
os.chdir(r"C:\Users\preet\.vscode\cipherpython\cyphor python week 4")
print(os.listdir())
filehere= os.walk(r"C:\Users\preet\.vscode\cipherpython\cyphor python week 4")

for current_path , follow_names, file_nmaes in filehere:
    print(f'current path : {current_path}')
    # print(f'folder names : {}')
    # print(f'file names : {}')

# os.rmdir('file1')



