'''
2023.05.10
정성훈
#문제정의
    입력받은 숫자가 소수인지 아닌지 판별하는 프로그램
#문제분석
    변수-숫자(num)
#알고리즘
    1.변수 초기화
        num에 정수입력
    2.논리(반복안에 선택포함)
        (반복) for i in range(2,num+1):
                (선택) num%i=0:
                    break
               if num==i:
                    (소수)
               else:
                    (소수아님)       
'''

num=int(input("소수 검증 숫자 : "))
for i in range(2,num+1):
    if num%i==0:
        break
if num==i:
    print('{}는 소수.'.format(num))
else:
    print('{}는 소수아님.'.format(num))
