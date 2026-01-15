#문제
#어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램
#문자열에 포함되는 괄호는 소괄호("()")와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.

#모든 왼쪽 소괄호는 오른쪽 소괄호와만 짝을 이뤄야 한다.
#모든 왼쪽 대괄호는 오른쪽 대괄호와만 짝을 이뤄야 한다.
#모든 오른쪽 괄호들은 자신과 짝을 이룰 수 있는 왼쪽 괄호가 존재한다.
#모든 괄호들의 짝은 1:1매칭만 가능하다. 즉, 괄호 하나가 둘 이상의 괄호와 짝지어지지 않는다.
#짝을 이루는 두 괄호가 있을 때, 그 사이에 있는 문자열도 균형이 잡혀야 한다.


#입력
#각 문자열은 마지막 글자를 제외하고 영문 알파벳,공백,소괄호,대괄호로 이루어져 있으며,
#온점(".")으로 끝나고, 길이는 100글자보다 작거나 같다.
#입력의 종료 조건으로 맨 마지막에 온점 하나(".")가 들어온다.

#출력
#각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를 아니면 "no"를 출력한다.


import sys
input = sys.stdin.readline

while True:
    line = input().rstrip()#엔터치면 그게 line변수에 들어간다.rstrip()을 하면 sys.stdin.readline을 해서 들어오는 개행문자(\n)을 
    if line == ".":#내용이 점 하나뿐이면?
        break#프로그램 종료!
    
    #이제 검사해야할 문장을 검사하는 로직을 짜야함.
    result=[]
    is_balanced = True#처음엔 균형이 맞음

    for char in line:
        if char == "(" or char =='[':
            result.append(char)
        elif char == ")":
            if not result or result[-1] !='(':#스택이 비었거나 맨 마지막이 (가 아님
                is_balanced = False
                break
            else:
                result.pop()
        elif char == ']':
            if not result or result[-1] !='[':#스택이 비었거나 맨 마지막이 [가 아님
                is_balanced = False
                break
            else:
                result.pop()
    if is_balanced == True and not result:
        print("yes")
    else:
        print("no")