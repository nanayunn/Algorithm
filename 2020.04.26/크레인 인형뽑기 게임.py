def solution(board, moves):
    basket = []
    cnt = 0
    for a in moves :   
        for i in range(len(board[0])):
            j = a-1
            if board[i][j]==0:
                continue
            else:
                basket.append(board[i][j])
                board[i][j]=0
                
                for n in range(len(basket)-2):
                    if len(basket)==1:
                        break
                    elif basket[n]==basket[n+1]:
                        basket.pop(basket[n])
                        basket.pop(basket[n+1])
                        cnt+=2
                    else:
                        pass
                break
    answer = cnt
    return answer   


# def solution(board, moves):
#     basket = []
#     cnt = 0
#     for a in moves :    #range(len(moves)-1):
#         for i in range(len(board[0])):
#             #j = moves[a]
#             j = a-1
#             #print(j)
#             if board[i][j]==0:
#                 continue
#             else:
#                 basket.append(board[i][j])
#                 print(board[i][j])
#                 board[i][j]=0
#                 print(board[i][j])
                
#                 # for n in range(len(basket)-1):
#                 #     if basket[n]==basket[n+1]:
#                 #         basket.pop(basket[n])
#                 #         basket.pop(basket[n+1])
#                 # cnt+=1
#                 break
#     #for n in range(1, len(basket)-1):
#         #if basket[n]==basket[n-1]:
#             #cnt+=1
            
#     answer = basket
#     return answer

