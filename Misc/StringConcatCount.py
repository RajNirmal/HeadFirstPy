str1 = 'abcdef'
str2 = 'efghij'
# str1 = input().strip()
# str2 = input().strip()
i = str2.find(str1[-1]) 

if i is -1:
    print(len(str1+str2))
else:
    count = 0
    str3 = ''
    for a in range(i,-1,-1) :
        str3 = str3+str2[a]
    str3 = str3[::-1]
    if str1.endswith(str3):
        print(str3+" found")
        print(len(str1+str2)-len(str3))
    else:
        print(len(str1+str2))
    
