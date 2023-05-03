'''
2023.05.03
정성훈
1~10까지 합계구하기
'''

#while반복
i=1 #반복 횟수 초기화
sum=0 #합계
while i<=10: # 반복 조건
    sum=sum+i
    i=i+1 #i 1증가
print('1~10까지의합계 : ',sum)

print()

#for반복
sum1=0
for j in range(1,11): #반복조건
    sum1=sum1 + j #합계 구하기
print('1~10까지의합계 : ',sum1)
