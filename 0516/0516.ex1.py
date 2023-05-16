'''
2023.05.16
정성훈
파일 입출력
'''

ft=open("C:/data/test.txt","w") #파일 객채 ft 생성(쓰기)

for i in range(1,11): #10번 반복
    ft.write('%d번째 줄입니다.\n'%i) #ft에 i출력

ft.close() #파일종료

