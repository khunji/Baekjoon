A,B = map(int, input().split())
#구간의 시작과 끝
#A번째 숫자부터 B번째 숫자까지

i=1
j=1
new_A=A
new_B=B
original_A=0
original_B=0
need_A=0
need_B=0

while True:
    new_A -= i
    if new_A <= 0:
        original_A = i #orginal_A는 A번째 자리에 있는 수
        need_A=i+new_A
        break
    i+=1
  

while True:
    new_B-=j
    if new_B <= 0:
        original_B = j
        need_B=j+new_B
        break
    j+=1


#일단 A번째 수가 무엇인지 B번째 수가 무엇인지 알아내는 방법은 찾음.
#그런데 그 사이에 특정 숫자가 몇 개인지를 알아내야 함.
total=0

if original_A  == original_B:
    total = original_A * (need_B - need_A + 1)

else:

    total += original_A * (original_A-need_A+1)

    for k in range(original_A+1, original_B):
        total += k*k
    
    total+= original_B * need_B

print(total)