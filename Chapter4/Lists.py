man = []
other = []
try:
    the_file = open("sketch.txt")
    for each_line in the_file:
        try:
            (Name,Line) = each_line.split(':')
            Line = Line.strip()
            if Name == "Man":
                man.append(Line)
            elif Name == "Other Man":
                other.append(Line)
        except ValueError:
            pass
except IOError as err:
    print("Shit some error occured. The error is "+str(err))
try:
    Man1File = open("Man1File.txt","w")
    Man2File = open("Man2File.txt","w")
    print(man,file = Man1File)
    print(other, file = Man2File)
except IOError:
    print("The file is missing dumb ass idiot. Stop trying to open it")
finally:
    Man1File.close()
    Man2File.close()
