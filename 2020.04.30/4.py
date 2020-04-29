T = 10
for y in range(T+1):
    t = int(input())
    i = list(map(int,input().split()))
    lst = []
    #while len(i) in range(t+1):
    for a in range(2,len(i)-2):
        b = [i[a-2],i[a-1],i[a+1],i[a+2]]
        c = max(b)            
        if i[a]-c>0:
            d = i[a]-c
            lst.append(d)
            a+=1
        else:
            a+=1
            
    print('#{}'.format(y),sum(lst))
         
