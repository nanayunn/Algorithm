import queue

T = int(input())
a, b = map(int,input().split())

q= queue.Queue()
# 1회
# 1등  5000000
# 2~3등 3000000
# 4~6등 2000000
# 7~10등 500000
# 11~15등 300000
# 16등~21등 100000

# 2회
# 1등 5120000
# 2~3등 2560000
# 4~7등 1280000
# 8~15등 640000
# 16~31등 320000

for i in range(T):
    
    for a in range(101):  
        if a ==1:
            n = 5000000
        elif a in range(2,4):
            n = 3000000
        elif a in range(4,7):
            n = 2000000
        elif a in range(7,11):
            n = 500000
        elif a in range(11,16):
            n = 300000
        elif a in range(16,22):
            n = 100000
        else:  
            a = 0

        if b == 1:
            m = 5120000
        elif b in range(2,4):
            m = 2560000
        elif b in range(4,8):
            m = 1280000
        elif b in range(8,16):
            m = 640000
        elif b in range(16,32):
            m = 320000
        else:
            m = 0
    p = n+m    
    queue.put(p)        
   
    for j in range (T):
        print(queue.get[j])              
