'''
2023.05.16
정성훈
파일 출력 - writelines() -> 리스트나 튜플 같은 자료형을 파일에 저장
                        -> 리스트나 튜플의 자료형은 문자여야 한다
         - write() -> 문자열만 파일에 출력  
'''

L1=['충청남도','충청북도\n','전라남도','전라복도\n','경상남도','경상북도\n']

L2=[1,2,3,4,5]

with open('C:/data/linetest.txt','w') as f:

    f.writelines(L1)