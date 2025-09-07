#예를 들어, ljes=njak은 크로아티아 알파벳 6개
# (lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 
# 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
#dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다.
#위 목록에 없는 알파벳은 한 글자씩 센다.


#입력
#첫째 줄에 최대 100글자의 단어가 주어진다. 알파벳 소문자와 '-','='로만
#이루어져 있다.

croatia_alphabet = ['c=','c-','dz=','d-','lj','nj','s=','z=']

count1=0
count2=0

s=input()


for i in croatia_alphabet:
    s = s.replace(i,'*')
    

for i in s:
    if i != '*':
        count2+=1
    else:
        count1+=1
print(count1+count2)
