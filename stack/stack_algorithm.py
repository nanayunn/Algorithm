def push(n):
    lst.append(n)
def pop(n):
    try:
        print(lst.pop())    
    except:
        print(-1)
def size():
    return len(lst)
def empty():
    a = 1 if size()==0 else 0
    print(a)
def top():
    try:
        print(lst[-1])
    except:
        print(-1)         

a = int(input())
lst = []
for _ in range(a):
    cmd = input().split()
    if cmd[0]=='push':
        push(cmd[1])
    elif cmd[0]==pop:
        pop()
    elif cmd[0]=='size':
        print(size())
    elif cmd[0]=='empty':
        empty()
    elif cmd[0]=='top': 
        top()              