try:
    the_file = open("sket2ch.txt")
    # each_line = the_file.readline();
    for each_line in the_file:
        try:
            (role,line) = each_line.split(":",1)
            print(role ,end=" ")
            print("said : ",end='')
            print(line, end ="")
        except:
            pass
    the_file.close();
except:
    print("The file is missing")

