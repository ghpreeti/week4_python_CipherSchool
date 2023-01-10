import os, shutil

#NOTE: you can write every single extension inside tuples

dict_extensions = {
    'audio_extensions' : ('mp3','m4a', 'wav','flac'),  
    'videos_extensions' : ('mp4','mkv', 'MKV', 'flv', 'mpeg'),
    'documents_extensions' : ('.doc','.pdf','.txt'),
}


audio_extensions = ('mp3','m4a', 'wav','flac')
videos_extensions = ('mp4','mkv', 'MKV', 'flv', 'mpeg')
documents_extensions = ('.doc','.pdf','.txt')


folderpath = input("Enter folder path : ")

def file_finder(folder_path,file_extensions):
    for file in os.listdir(folder_path):
        for extensions in file_extensions:
            if file.endswith(extensions):
                file.append(file)
    return file     
print(file_finder(folderpath,videos_extensions))    

for extension_type, extension_tuple in dict_extensions.items():
    print('calling file finder')
    print(file_finder(folderpath,extension_tuple))


