'''
2023.05.03
정성훈
#문제정의
    1~입력받은 숫자까지의 합계 구하기
#문제분석
    변수 num(입력받은 수), total(합계)
#알고리즘
    1.변수 선언
        num에 정수 입력받기
        total=0
    2.논리(반복)
        (조건)for i in range(1,num+1):
'''
num=int(input('수 : '))

#for반복문
total=0
for i in range(1,num+1):
    totoal=total+i
print('1~{}까지의 합계 : '.format(num,total))

print()

#while반복문
j=1
total1=0
while j<=num:
    total1=total1+j
    j=j+1
print('1~{}까지의 합계 : '.format(num,total1))

