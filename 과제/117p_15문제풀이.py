'''
2023.04.05 과제2
정성훈
117p_15번 문제풀이
'''

tax=int(input('자동차 세금: ')) #자동차 세금 입력

add=tax * 0.03 #가산금 계산
total= tax + add #총 세금 계산

print('자동차세금이 {}이고, 가산금이{}일때, 총 세금은 {}이다.'.format(tax,add,total))
