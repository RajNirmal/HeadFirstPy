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
    jamesList = [sanitize(each_t) for each_t in james]
    julieList = [sanitize(each_t) for each_t in julie]
    mikeyList = [sanitize(each_t) for each_t in mikey]
    sarahList = [sanitize(each_t) for each_t in sarah]
    print(sorted(jamesList))
    print(sorted(julieList))
    print(sorted(mikeyList))
    print(sorted(sarahList))
except IOError as err:
    print("The error is "+ str(err))