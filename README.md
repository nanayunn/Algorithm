# 스택

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

```python
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

***

# 제로 성공

[백준](https://www.notion.so/a9255296b5464705a7f6dcaf0cad7753)

## 문제

나코더 기장 재민이는 동아리 회식을 준비하기 위해서 장부를 관리하는 중이다.

재현이는 재민이를 도와서 돈을 관리하는 중인데, 애석하게도 항상 정신없는 재현이는 돈을 실수로 잘못 부르는 사고를 치기 일쑤였다.

재현이는 잘못된 수를 부를 때마다 0을 외쳐서, 가장 최근에 재민이가 쓴 수를 지우게 시킨다.

재민이는 이렇게 모든 수를 받아 적은 후 그 수의 합을 알고 싶어 한다. 재민이를 도와주자!

## 입력

첫 번째 줄에 정수 K가 주어진다. (1 ≤ K ≤ 100,000)

이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며, 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.

정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

## 출력

재민이가 최종적으로 적어 낸 수의 합을 출력한다.

## 예제 입력 1

```
4
3
0
4
0
```

## 예제 출력 1

```
0
```

## 예제 입력 2

```
10
1
3
5
4
0
0
7
0
0
6
```

## 예제 출력 2

```
7
```

# 풀이

```python
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
    print(sum(stack))
```

1. TestCase의 값 K 변수를 선언

2. 재민이가 적을 숫자를 입력할 stack 배열 생성

3. K 범위 안에서 도는 for문

   1. 재민이가 적을 숫자 변수를 선언
   2. 만약 숫자가 0이면 배열 뒤에서 첫번째 숫자를 삭제한다.(pop)
   3. 이외의 숫자가 입력되면 배열에 추가한다.

   K 범위 만큼 1~3을 반복

4. for문이 종료된 뒤 stack이 비었다면 0을 출력한다.

5. 만약 stack이 비어있지 않다면 stack에 남은 숫자들을 합산하여 출력한다.



***

# 큐

> FIFO(First In First Out)

- Put(순서대로 데이터 저장)
- Get(저장 순서대로 데이터 출력)

1. InitializeQueue : 초기화
2. Put()&Get()
3. 입구 (Rear) 출구(Front)

- 자료구조는 배열로 하는 것이 편하다.