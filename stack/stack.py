K = int(input())
stack = []

for _ in range(K):
    num = int(input())

    if (num ==0):
        del stack[-1]
    else:
        stack.append(num)
          
if not stack:
    print(0)
else:
    print(stack)    
