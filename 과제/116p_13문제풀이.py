'''
2023.04.05 과제1
정성훈
116p_13번 문제풀이
'''

pay=int(input('음식금액 : ')) #음식금액 입력

vat=pay * 0.1 #부가세 계산
dish=pay + vat #식사금액 계산

print('음식금액이 {}이고, 부가세가{}일때, 식사금액은 {}이다.'.format(pay,vat,dish))
