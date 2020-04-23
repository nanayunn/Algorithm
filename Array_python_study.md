# 2차원 배열

- 1차원 리스트를 묶어놓은 리스트
- 2차원 이상의 다차원 리스트는 차원에 따라 index를 선언
- 2차원 리스트의 선언 : 세로길이(행), 가로길이(열)

    arr = [[0,1,2,3],[4,5,6,7]]

- 리스트의 초기화

    arr = [0,0,0,0,0]
    arr = [0]*5 #[0,0,0,0,0]
    arr = [i for i in range(2,9) if i%2==0] #[2,4,6,8]
    
    brr = [[1,2,3],[1,2,3],[1,2,3]]
    brr = [[1,2,3] for i in range(3)] #[[1,2,3],[1,2,3],[1,2,3]]
    brr = [[i,j] for i in range(3) for j in range(2)]
    #[[0,0],[0,1],[1,0],[1,1],[2,0],[2,1],[2,2]]

 

- 2차원 리스트 입력받기
1. 첫째줄에 n행 m열,

    둘째줄부터 n*m의 행열 데이터가 주어질 경우

    #n행 m열 리스트
    
    n, m = map(int, input().split())
    
    mylist = [0 for _ in range(n)]
    for i in range(n):
    	mylist[i]=list(map(int, input().split()))

2. 

    n, m = map(int, input().split())
    mylist = []
    for i in range(n):
    	mylist.append(list(map(int, input().split())))

3.

    n, m = map(int, input().split())
    mylist = [list(map(int, input().split())) for _ in range(n)]

- 2차원 리스트에서 원하는 데이터의 위치 찾기
1. 주어진 데이터에서 1이 입력된 [행, 열]의 위치 찾기

    n, m = map(int, input().split())
    newlist = []
    mylist = [0 for _ in range(n)]
    for i in range(n):
    	mylist[i] = list(map(int, input().split()))
    		for j in range(m):
    			if mylist[i][j]==1:
    					newlist.append([i,j])
    

2. 

    n, m = map(int, input().split())
    mylist = [list(map(int, input().split())) for _ in range(n)]
    newlist = [(i,j) for i in range(n) for j in range(m) if mylist[i][j]==1]

- 리스트 순회

> n*m 리스트의 모든 원소를 빠짐없이 조사하는 법

1. 행 우선 순회

    arr =[[1,2,3,4],
    			[5,6,7,8],
    			[9,10,11,12]]
    for i in range(len(arr)):
    		for j in range(len(arr));
    				arr[i][j]

2. 열 우선 순회

    arr =[[1,2,3,4],
    			[5,6,7,8],
    			[9,10,11,12]]
    for j in range(len(arr)):
    		for i in range(len(arr));
    				arr[i][j]

3. 지그재그 순회

    arr =[[1,2,3,4],
    			[5,6,7,8],
    			[9,10,11,12]]
    for i in range(len(arr)):
    		for j in range(len(arr));
    				arr[i][j+(m-1-2*j)*(i%2)]

- 델타를 이용한 2차 리스트 탐색
1. 2차 리스트의 한 좌표에서 네방향의 인접 리스트 요소를 탐색할 때 사용하는 방법
2. 델타 값은 한 좌표에서 네 방향의 좌표와 x, y의 차이를 저장한 리스트로 구현
3. 델타 값을 이용하여 특정 원소의 상하좌우에 위치한 원소에 접근할 수 있음
4. ** 이차원 리스트의 가장자리 원소들 의 인덱스 체크, 범위 제한 필요

    arr[0...n-1][0...n-1] #2차원 리스트
    dx = [0,0,-1,-1]
    dy = [-1,1,0,0]
    for x in range(len(arr)):
    		for y in range(len(arr)):
    				for i in range(4):
    						testX = x + dx[i]
    						testY = y + dy[i]
    						print(arr[testX][testY])

- 전치 행렬
    - 행과 열의 값이 반대인 행렬을 의미(대각선을 기준으로)

    for i in range(3):
    		for j in range(3):
    				if i<j:
    						arr[i][j],arr[j][i] = arr[j][i],arr[i][j]

** 모든 좌표에 대하여 행과 열의 값을 바꾸면 360도 돈거랑 똑같음

- **zip** (iterable)
    - 동일한 개수로 이루어진 자료형들을 묶어주는 역할을 하는 함수

    alpha = ['a','b','c']
    index = [1,2,3]
    alph_index = list(zip(alpha,index))
    print(alph_index)
    >>>>[('a',1),('b',2),('c',3)]

    arr = [[1,2,3],[4,5,6],[7,8,9]]
    print(list(zip(*arr)))
    >>>[(1,4,7),(2,5,8),(3,6,9)]

- zip(*matrix)
    - 전치행렬을 만드는 것과 같음