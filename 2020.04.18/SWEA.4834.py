#SWEA.4834
# [문제]
# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 
# 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  
# ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. 
# ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. 
# (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 
# 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

# list 형식에 쓰면 딕셔너리의 형태로 각 요소의 갯수를 구해준다
from collections import Counter

T = int(input())
for t in range(1,T+1):
    N = int(input())
    a = str(input())
    ai = list(a)
    count = Counter(ai)
    cnt = 0
    arr = []
    #딕셔너리 내의 최빈수의 갯수 값을 찾는다
    max_count = max(count.values())
    #딕셔너리 내의 value값을 list화
    count_list = list(count.values())
    #딕셔너리 value 값 리스트에서 최빈수 값의 갯수를 
    #세고, 1보다 크면 최빈수 값을 갖고 있는 key를 
    #arr 리스트에 추가해준 뒤 가장 큰 값을 구해 출력한다.
    if count_list.count(max_count)>1:
        for keys, values in count.items():
            if values == max_count:
                arr.append(keys)
            
        print(("#{0} {1} {2}").format(t,max(arr),max_count))
    
    else:
        for keys, values in count.items():
            if values == max_count:
                print(("#{0} {1} {2}").format(t,keys,values))
            
