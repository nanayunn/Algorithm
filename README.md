# **스택**

### **스택이란?**

> 입,출력을 한 방향으로 제한한 자료구조

바닥에서 데이터를 차곡차곡(push)

최신 데이터부터 차례로 가져옴(pop)LIFO(Last in First Out)

### **구현 방법**

- 메모리를 쌓을 메모리 공간(배열 or 링크드 리스트)
- 하위 자료구조

### **Python Stack**

### **기본 구조 및 함수 구현**
```
    class Stack:
    def **init**(self):
    self.len = 0
    self.list = []

    def push(self, num):
        self.list.append(num)
        self.len += 1
    
    def pop(self):
        if self.size() == 0:
            return -1
        pop_result = self.list[self.len - 1]
        del self.list[self.len - 1]
        self.len -= 1
        return pop_result
        
    def size(self):
        return self.len
        
    def empty(self):
        return 1 if self.len == 0 else 0
        
    def top(self):
        return self.list[-1] if self.size() != 0 else -1

    num = int(input())
    stack = Stack()
    while(num > 0):
    num -= 1
    input_split = input().split()

    op = input_split[0]
    
    if op == "push":
        stack.push(input_split[1])
    elif op == "pop":
        print(stack.pop())
    elif op == "size":
        print(stack.size())
    elif op == "empty":
        print(stack.empty())
    elif op == "top":
        print(stack.top())
    else:
        print("unacceptable op")
 ```
