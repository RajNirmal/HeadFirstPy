#Your code below
str1 = input().strip()
str2 = input().strip()
# print(str1+"\n"+str2)
if len(str1) is not len(str2):
    print("NO")
    quit()

def checkISO(str1,str2):
    dicts = {}
    for a in range(0,len(str1)):
        chars = str1[a]
        if chars in dicts.keys():
            if str2[a] is dicts[chars]:
                pass
            else:
                return False
        else:
            dicts[chars] = str2[a]
        print(dicts)
    return True
flag1 = checkISO(str1,str2)
flag2 = checkISO(str2,str1)
if flag1 and flag2:
    print("YES")
else:
    print("NO")