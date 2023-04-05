'''
2023.04.05
정성훈
117p 14번 문제풀이
'''

sub1=int(input('과목1점수 : ')) #과목1 점수입력
sub2=int(input('과목2점수 : ')) #과목2 점수입력
sub3=int(input('과목3점수 : ')) #과목3 점수입력
sub4=int(input('과목4점수 : ')) #과목4 점수입력
sub5=int(input('과목5점수 : ')) #과목5 점수입력

total=sub1+sub2+sub3+sub4+sub5 #합계 구하기
avg=total/5 #평균 구하기

print('5과목의 합계는{}이고, 평균은{}이다.'.format(total,avg))

