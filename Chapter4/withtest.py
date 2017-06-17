import pickle
list1 = []
list2 = []
try:
    with open("Man1File.txt","rb") as data, open("Man2File.txt","rb") as data2:
        list1 = pickle.load(data)
        list2 = pickle.load(data2)
except IOError as  err:
    print("Shit Happened,"+str(err))
except pickle.PickleError as err2:
    print("Huge Shit happened"+str(err2))
print(*list1)
print("\n")
print(*list2)
    