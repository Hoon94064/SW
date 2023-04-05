'''
2023.04.05
정성훈
116p_9번 문제풀이
'''

sal=int(input('본봉 : ')) #본봉 입력
allo=int(input('수당 : ')) #수당 입력

tax=(sal+allo)*0.2 #세금 계산
total_sal=sal + allo - tax #수령액 계산

print('홍길동의 본봉이 {}이고, 수당이{}일때, 실수령액은 {}이다.'.format(sal,allo,total_sal))
