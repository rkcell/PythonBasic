import pickle
import struct
#for binary

f = open("test.txt","r")
# for line in f:
#     print(line.strip())

lines=f.readlines()
print(len(lines))




# import os
#
# folder_name="MyFolder"
# os.mkdir(folder_name)
# os.chdir(folder_name)
# f= open("myfile.txt", "a")




# from pathlib import Path
# p= Path.cwd()
# print(p)
#
# import os
# os.chdir("/home")
# p= Path.cwd()
# print(p)

# f = open("test.txt", "a")
# # for x in f:
# #     print(x)
# f.write("\nHellooo")
# f.close()
# import os
# if os.path.isfile("test.txt"):
#     print("File existed and deleted!")
#     os.remove("test.txt")
# else:
#     print("File does not exist", os.name)

#file.seek(0)