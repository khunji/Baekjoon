N = int(input()) #파일 이름의 개수
file=[] #파일 이름들을 저장할 리스트

for i in range(N):
    s = input()
    file.append(s)
    
result = list(file[0]) #첫 번째 결괏값과 파일에 있는 다른 이름들을 비교하면서
# 만약에 다른 부분이 나오면 그 부분을 ?로 바꾸자.
#result = ['c','o','n','f','i','g','.','s','y','s']

for i in range(1,N):
    for j in range(len(result)):
        if result[j] == file[i][j]:
            continue
        else:
            result[j]='?'

print(''.join(result))
    