'''
2023.04.19
정성훈
성별, 키, 몸무게를 입력받아 각각 '표준체중', '과체중', '비만체중'을 출력하고,
성별이 맞지 않는경우 '성별 입력이 잘못 되었습니다.' 를 출력하는 프로그램
#문제분석
    변수 : 성별(sex), 키(height)cm, 몸무게(weight)kg, 평균체중(avg)
    수식 : 남자 - avg = height * height * 22
           여자 - avg = height * height * 21
           비만도 - BMI = weight / avg *100
#알고리즘
    1.변수선언 : sex에 성별입력, height, weight에 실수로 입력받기
    2.논리 (내포된 선택)
        if (sex==M) and (sex==m):
            avg = height * height * 22
            BMI = weight / avg *100
            if BMI>=120:
                ('비만 체중')
            elif 110<=BMI<=119:
                ('과체중')
            else:
                ('표준 체중')

        elif (sex==F) and (sex==f):
            avg = height * height * 21
            BMI = weight / avg *100
            if BMI >=120:
                ('비만')
            elif 110<= BMI <=119:
                ('과체중')
            else:
                ('표준 체중')
'''     

sex=input('성별입력("M or m" 또는 "F or f") : ') #성별 문자로 입력
height=float(input('키 입력(cm) : ')) / 100 #키 실수로입력 (m로 단위 변화)
weight=float(input('몸무게 입력(kg) : ')) #몸무게 실수로 입력

if (sex=='M' or sex=='m'): #남자
    avg = height * height * 22
    BMI = weight / avg * 100
    if BMI >= 120:
        print('비만 체중')
    elif 110<= BMI <=119:
        print('과체중')
    else:
        print('표준 체중')
                
elif (sex=='F' or sex=='f'): #여자
    avg = height * height * 21
    BMI = weight / avg * 100
    if BMI >=120:
        print('비만 체중')
    elif 110<= BMI <=119:
        print('과체중')
    else:
        print('표준 체중')
else: # 성별이 잘못된 경우
    print('성별 입력이 잘못 되었습니다.')
