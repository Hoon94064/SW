'''
2023.05.03
정성훈
#문제정의
    구구단 출력(중첩 반복)
#문제분석
    변수 - dan,i
#알고리즘
    논리(반복-중첩 반복(for))
    (조건) for dan in range(2,10): #단 반복
                제목출력
                for i in range(1,10) #단 안에서 곱하는 수 반복
                    구구단 출력
'''

for dan in range(2,10): #단 반복
    print('###',dan,'단###')
    for i in range(1,10): #단 안에서 곱하는 수 반복
        print('{}*{}={}'.format(dan,i,dan*1)) # print(dan,"*",i,"=",dan*i)


'''
dan=2
i=1

while dan<=9:
    print('###',dan,'단###')
    while i<=9:
        print(dan,"*",i,"=",dan*i)
        i=i+1
        continue
    dan=dan+1
'''
