'''
2023-04-11
정성훈
선택문-if~else~else
성적이 90이상이면 'A학점' 80이상 90미만이면 'B학점' 70이상 80미만이면 'C학점' 70미만이면 'F학점'
'''

score=int(input('성적 입력:'))

if score>=90: #조건1
    print('A학점') #조건1이 참인 경우
elif score>=80: #조건2
    print('B학점') #조건2가 참인 경우
elif score>=70: #조건3
    print('C학점') #조건3이 참인 경우
else:
    print('F학점') #조건1,2,3이 모두 거짓인 경우


