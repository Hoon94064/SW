'''
2023.04.04
정성훈
표준출력(print) format 연습
'''

print('이름은 {}이고 나이는{}입니다.'.format('정성훈',25))
print('이름{name}, 나이{age}, 주소{add}'.format(add=' 부산 신라대학교',name=' 정성훈',age= 26))
print('The lucky number is ({:14})'.format(7777)) #숫자는 기본 오른쪽 정렬
print('The lucky number is ({:<14})'.format(7777)) #:< 숫자 왼쪽 정렬

