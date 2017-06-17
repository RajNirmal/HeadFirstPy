jamesList = []
julieList = []
mikeyList = []
sarahList = []
def sanitize(data):
    if '-' in data:
       splitter = '-' 
    elif ':' in data:
        splitter = ':'
    else:
        return data
    (mins,sec) = data.strip().split(splitter)
    # print (mins+'.'+sec)
    return (mins+'.'+sec)
    # return data2

try:
    with open("james.txt") as data:
        james = data.readline().strip().split(',')
    with open("julie.txt") as data:
        julie = data.readline().strip().split(',')
    with open("mikey.txt") as data:
        mikey = data.readline().strip().split(',')
    with open("sarah.txt") as data:
        sarah = data.readline().strip().split(',')
    for a in james:
        jamesList.append(sanitize(a))
    for a in julie:
        julieList.append(sanitize(a))
    for a in mikey:
        mikeyList.append(sanitize(a))
    for a in sarah:
        sarahList.append(sanitize(a))
    print(sorted(jamesList,reverse=Trues))
    print(sorted(julieList))
    print(sorted(mikeyList))
    print(sorted(sarahList))
except IOError as err:
    print("The error is"+ str(err))
