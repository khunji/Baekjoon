#입력 전체 받기
n = int(input())
target=[]   #스택 수열의 원소를 넣을 배열
for _ in range(n):
    target.append(int(input())) #스택 수열을 한 번에 배열에 저장하기

#여기서부터는 target의 원소 하나하나를 순회하면서 op에 필요한 연산(+,-)을 저장할 것
next_push = 1   #스택에 push는 무조건 오름차순으로 해야 하니 1로 초기화해두자.
stack=[]        #스택 배열 
op=[]           #얘는 +,-넣을 배열

for i in target:
    while next_push <= i:   #next_push가 target보다 커지면 안된다.
        stack.append(next_push)
        op.append("+")
        next_push+=1

    if stack[-1] == i:
        stack.pop()
        op.append("-")
    
    else:
        print("NO")
        exit()
        
for x in op:
    print(x)
