'''
2023.04.18
정성훈
p145 7번 문제풀이
두 정수를 입력받아 두정수의 연산 값(x>y -> x//y , x<y -> x+y , x=y -> x*y)이 출력되는 프로그램
단, 나눗셈 몫 계산할 때 y는 0이 아니어야 됨.
#문제분석
    변수 : 정수1(x), 정수2(y)
    수식 : x>y = x//y (y>0) , x<y = x+y , x==y = x*y
#알고리즘
    1.변수선언
        x, y에 정수 입력받기
    2.논리
        if x>y and y>0:
            'x // y'
        elif x<y:
            'x + y'
        elif x==y:
            'x * y'
        else:
            y의 값이 0입니다.
'''
x=int(input('x의 값을 입력해주세요 : '))
y=int(input('y의 값을 입력해주세요 : '))

if (x>y) and (y>0):
        print('{} // {} = {}'.format(x,y,x//y))
elif x<y:
    print('{} + {} = {}'.format(x,y,x+y))
elif x==y:
    print('{} * {} = {}'.format(x,y,x*y))
else:
    print('y의 값이 0입니다.')
    