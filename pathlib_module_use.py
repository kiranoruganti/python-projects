from pathlib import Path
path1=Path("bank management system.py")

print(path1)#prints file name

print(path1.home())#gets home directory of current user (c:\users\kiran)

print(path1.exists())#if any data or code exits in file returns True otherwise returns False if u have doubt erase data in file and see
#Checking Whether the path represents tge path to a file

print(path1.is_file())#path is to aa file

print(path1.is_dir())# path is to a file not directory

print(path1.suffix)#gives extension of the file(.py)

print(path1.stem)#prints  full name of the file

print(path1.parent)# gives . which means present working directory i.e the codingrad project file

print(path1.absolute())# gives the absolute path of the file

# import pickle
# lst=["sdbbjqebfjqj",16646]
# abc=open("abcd.txt","wb")
# # pickle.dump(lst,"abcd.txt")
#
# abc.close()