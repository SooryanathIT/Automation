import os

input_file_path = input("> Enter the file path : ")

print("File name : " , input_file_path)

if os.path.exists(input_file_path) : print("File Exists")

else : print("File Doesn't exists")

print("File size of noms.txt ->  " , os.path.getsize('noms.txt'))