import os

if os.path.exists("sketcha.txt"):
    the_file = open("sketch.txt")
    # each_line = the_file.readline();
    for each_line in the_file:
        if each_line.find(':') is not -1:
            (role,line) = each_line.split(":",1)
            print(role ,end=" ")
            print("said : ",end='')
            print(line, end ="")
        else:
            print(each_line)

    the_file.close();
else:
    print("the file is missing")