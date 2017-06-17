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
            myData = data.readline().strip().split(',')
    except IOError as err:
        print("The error is "+ str(err))
        return
    dataDict = {}
    dataDict['Name'] = myData.pop(0)
    dataDict['DOB'] = myData.pop(0)
    dataDict['Times'] = sorted([sanitize(each_t) for each_t in myData])
    return dataDict

def printStuff(dickDict):
    print("The fastest times of "+dickDict['Name']+"\nThe date of birth is "+dickDict['DOB']+"\nThe fastest times are "+dickDict['Times'][0:3])    

sarahDict = getData("sarah")
jamesDict = getData("james")
julieDict = getData("julie")
mikeyDict = getData("mikey")


