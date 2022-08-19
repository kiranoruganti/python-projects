'''
pickle is a module
python objects(list,dict) ni byte stream ki convert chesedhanni pickling antaru and
byte stream nunchi objects ki convert cheyadam ni unpickling antaru

pickling=serializing and unpickling=de-serializing

pickle.dump()=obj to byte stream convert chestadi(pickling)
pickle.load()= byte stream ni obj loki covert chesthadi(unpickling)
'''



import pickle

Mylist=["kiran","teja"]
#pickling
with open("file.txt","wb") as  f:   #file=f ani shortcut chesam    wb=write binary
    pickle.dump(Mylist,f) #file.txt ane file create aithadi

#unpickling
unpick=open("file.txt","rb") #rb=read binary

m=pickle.load(unpick)  #load function use cheskoni unpickle chesnam file

print(m)