def isValid(str) :
    length = len(str)
    total = 0
    for i in range(length) :
        if total < 0 :
            print("NO")
            return -1
        
        if str[i] == '(' :
            total += 1
        else :
            total -= 1
    if total == 0 :
        print("YES")
        return 0
    else :
        print("NO")
        return -1
    
T = int(input())
for i in range(T) :
    isValid(input())