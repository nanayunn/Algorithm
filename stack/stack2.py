T = int(input())
stack = []
stack2 = [] 

for _ in range(T):
    v = str(input())
    for i in range(len(v)):
        if v[i] ==")" and stack!=[]:
            del stack[-1]                        
        else:
            stack.append(v[i])

    if stack==[]:
        stack2.append("YES")
    else :
        stack2.append("NO")
    stack.clear()
for j in range (T):
    print(stack2[j])               