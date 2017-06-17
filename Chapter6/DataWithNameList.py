"""This is a function that will clean the data
    of anamoly. The : and - are replaced by . in this file"""
def sanitize(data):
    if '-' in data:
       splitter = '-' 
    elif ':' in data:
        splitter = ':'
    else:
        return data
    (mins,sec) = data.strip().split(splitter)
    return (mins+'.'+sec)

"""This is a function to read the data from the 
    disk and will return a list containing 
    the times"""
def getData(filename):
    try:
        with open(filename+"2.txt") as data:
            return (data.readline().strip().split(','))
    except IOError as err:
        print("The error is "+ str(err))


james = getData("james")
julie = getData("julie")
mikey = getData("mikey")
sarah = getData("sarah")

"""Clean the code before converting it to sorted format"""
(james_name,james_BD) = james.pop(0),james.pop(0)
(julie_name,julie_BD) = julie.pop(0),julie.pop(0)
(mikey_name,mikey_BD) = mikey.pop(0),mikey.pop(0)
(sarah_name,sarah_BD) = sarah.pop(0),sarah.pop(0)

"""This is the code to convert to list into a set
    A set will automatically convert the list data by
    removing the duplicates and the data is also sorted by
    using the sort function"""
jamesList = sorted(set(sanitize(each_t) for each_t in james))
julieList = sorted(set(sanitize(each_t) for each_t in julie))
mikeyList = sorted(set(sanitize(each_t) for each_t in mikey))
sarahList = sorted(set(sanitize(each_t) for each_t in sarah))
"""Print the first 3 items"""
print(james_name+" The 3 fast times are "+ str(jamesList[0:3]))
print(julie_name+" The 3 fast times are "+ str(julieList[0:3]))
print(mikey_name+" The 3 fast times are "+ str(mikeyList[0:3]))
print(sarah_name+" The 3 fast times are "+ str(sarahList[0:3]))
