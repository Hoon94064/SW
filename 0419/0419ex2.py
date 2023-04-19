'''
2023.04.19
정성훈
조건문을 사용하여 입력된 수가 양수, 0, 음수인지 판별하는 프로그램
#문제분석
    변수 : 숫자(num)
    수식 : num>0 , num==0 , num<0
#알고리즘 (단순if)
    1.변수선언 : num에 정수 입력받기
    2.논리(선택) 
        if num>0:
            ('양수')
        if num<0:
            ('음수')
        if num==0
            ('0')
#알고리즘 (다중if) 
    1.변수선언 : num에 정수 입력받기
    2.논리(선택)       
        if num>0:
            ('양수')
        elif num<0:
            ('음수')
        else:
            ('0')
'''
#단순if
num=int(input('숫자 입력 : '))

if num>0:
    print('입력값 {}는 양수입니다.'.format(num))
if  num<0:
    print('입력값 {}는 음수입니다.'.format(num))
if num==0:
    print('입력값 {}는 0입니다.'.format(num))

#다중if
num=int(input('숫자 입력 : '))

if num>0:
    print('입력값 {}는 양수입니다.'.format(num))
elif num<0:
    print('입력값 {}는 음수입니다.'.format(num))
else:
    print('입력값 {}는 0입니다.'.format(num))
