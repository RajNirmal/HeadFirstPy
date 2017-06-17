uniqueJames = []
uniqueJulie = []
uniqueMikey = []
uniqueSarah = []
def sanitize(data):
    if '-' in data:
       splitter = '-' 
    elif ':' in data:
        splitter = ':'
    else:
        return data
    (mins,sec) = data.strip().split(splitter)
    return (mins+'.'+sec)

try:
    with open("james.txt") as data:
        james = data.readline().strip().split(',')
    with open("julie.txt") as data:
        julie = data.readline().strip().split(',')
    with open("mikey.txt") as data:
        mikey = data.readline().strip().split(',')
    with open("sarah.txt") as data:
        sarah = data.readline().strip().split(',')
    jamesList = sorted([sanitize(each_t) for each_t in james])
    julieList = sorted([sanitize(each_t) for each_t in julie])
    mikeyList = sorted([sanitize(each_t) for each_t in mikey])
    sarahList = sorted([sanitize(each_t) for each_t in sarah])
    for each_t in jamesList:
        if each_t not in uniqueJames:
            uniqueJames.append(each_t)
    for each_t in julieList:
        if each_t not in uniqueJulie:
            uniqueJulie.append(each_t)
    for each_t in mikeyList:
        if each_t not in uniqueMikey:
            uniqueMikey.append(each_t)
    for each_t in sarahList:
        if each_t not in uniqueSarah:
            uniqueSarah.append(each_t)
    print(uniqueJames[0:3])
    print(uniqueJulie[0:3])
    print(uniqueMikey[0:3])
    print(uniqueSarah[0:3])
except IOError as err:
    print("The error is "+ str(err))