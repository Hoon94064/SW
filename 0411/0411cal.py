'''
2023.04.11
정성훈
cal문제풀이
'''

num1=int(input('숫자1:')) #숫자1 입력
oper=input('연산자:') #연산자 입력
num2=int(input('숫자2:')) #숫자2 입력

if oper=='+':
    print(num1+num2)
elif oper=='-':
    print(num1-num2)
elif oper=='*':
    print(num1*num2)
else:
    print(num1/num2)
