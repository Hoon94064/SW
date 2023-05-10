'''
2023.05.10
정성훈
#문제정의
    입력받은 숫자 만큼 줄 반복 하면서 별 찍기
#문제분석
    변수-숫자(num) 
#알고리즘
    1.변수 초기화
        num변수에 정수 입력
    2.논리(중첩 반복)
        (반복) for i in range(1,num+1):
                    (반복)for j in range(1,i+1)
                        별찍기
'''
num=int(input('숫자 입력 : '))

for i in range(1,num+1):
    for j in range(1,i+1):
        print("*",end="")
    print()


#거꾸로 출력
print('\n거꾸로 출력')

su=int(input('숫자 입력 : '))

for k in range(su,0,-1):
    for l in range(k,0,-1):
        print("*",end="")
    print()
