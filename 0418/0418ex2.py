'''
2023.04.18
정성훈
두 과목의 점수를 입력받아 두 과목 모두 75점 이상이고 총점이 180점 이상이면 '최우수 학생',
총점이 160점 이상이면 '우수학생', 총점이 150점 이상이면 '보통학생',
두 과목 모두 75점 미만이면 '분발합시다' 를 출력하는 프로그램
#문제분석
    변수 : 점수1(score1), 점수2(score2), 합계(total)
#알고리즘
    1.변수선언
        score1, socre2에 정수 입력받기
        total = score1 + score2
    2.논리(선택-중첩if)
        if (score1)>=75 and (score2)>=75:
            if(total)>=180:
            '최우수 학생'
            elif total>=160:
            '우수학생'
            elif total>=150:
            '보통학생'
            else:
            '분발합시다'
'''

score1=int(input('첫 번째 과목의 점수 입력 : ')) #점수1 정수로 입력
score2=int(input('두 번째 과목의 점수 입력 : ')) #점수2 정수로 입력
total = score1 + score2

'''
if (score1>=75) and (score2>=75) and (total>=180):
    print('최우수 학생')
elif 180>total>=160:
    print('우수 학생')
elif 160>total>=150:
    print('보통 학생')
else:
    print('분발합시다.')
'''

if (score1)>=75 and (score2)>=75: 
    if(total)>=180:
        print('최우수 학생')
    elif total>=160:
        print('우수학생')
    elif total>=150:
        print('보통학생')
else:
    print('분발합시다.')

    
