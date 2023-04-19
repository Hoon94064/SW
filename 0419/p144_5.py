'''
2023.04.18
정성훈
p144 5번 문제풀이
두 개의 숫자를 입력받아 두 번쨰 수가 첫 번째 수의 약수인지 아닌지 구분하는 프로그램
#문제분석
    변수 : 정수1(num1), 정수2(num2)
    수식 : num1%num2==0 (num2는 num1의 약수)
#알고리즘
    1.변수선언 : num1, num2에 정수 입력받기
    2.논리 (선택논리)
        if num1%num2 = 0:
            (num2는 num1의 약수입니다.)
        else:
            (num2는 num1의 약수가 아닙니다.)
'''

num1=int(input('첫 번째 정수를 입력하세요 : '))
num2=int(input('두 번째 정수를 입력하세요 : '))

if (num1%num2)==0:
    print('{}는 {}의 약수입니다.'.format(num2,num1))
else:
    print('{}는 {}의 약수가 아닙니다.'.format(num2,num1))
