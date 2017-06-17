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

class Athlete(list):
    def __init__(self,name , DOB = None, Times = []):
        list.__init__([])
        self.name = name
        self.DOB = DOB
        self.extend = Times
    
    def Top3Times(self):
        return sorted(sanitize(each_t) for each_t in self)[0:3]

   
"""This is a function to read the data from the 
    disk and will return a list containing 
    the times"""
def getData(filename):
    try:
        with open(filename+"2.txt") as data:
            myData = data.readline().strip().split(',')
    except IOError as err:
        print("The error is "+ str(err))
        return
    Name = myData.pop(0)
    DOB = myData.pop(0)
    Times = myData
    return Athlete(Name,DOB,Times)

def printStuff(dickDict):
    print("The fastest times of "+dickDict.name+"\nThe date of birth is "+dickDict.DOB+"\nThe fastest times are "+str(dickDict.Top3Times()))

sarahDict = getData("sarah")
jamesDict = getData("james")
julieDict = getData("julie")
mikeyDict = getData("mikey")
printStuff(sarahDict)
sarahDict.append('2.10')
printStuff(sarahDict)
sarahDict.extend(['2.01','2.11'])
printStuff(sarahDict)