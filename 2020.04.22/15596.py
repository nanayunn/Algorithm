def palin(a):
    str_list = list(a)
    str_list2 = str_list
    str_list3 = str_list2.reverse()

    if str_list ==str_list2:
        print(a)
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else:
        print("입력하신 단어는 회문(Peyalindrome)이 아닙니다.")    

s = input()
palin(s)