#그룹 단어 체커
#그룹 단어란? 각 문자가 연속해서 나타나는 경우만을 말한다. 
#ex:ccazzzzbb는 그룹단어, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹단어가 아니다.
#단어 N개를 입력받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

N = int(input())
current_N=N

for i in range(N):  #N번 입력받기
    word = input()
    for j in range(len(word)-1):
        if word[j]==word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            current_N-=1
            break
print(current_N)

