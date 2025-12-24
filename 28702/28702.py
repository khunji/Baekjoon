#문제
#FizzBuzz 문제
#i가 3의 배수이면서 5의 배수->"FizzBuzz"
#i가 3의 배수이지만 5의 배수가 아니면 "Fizz"
#i가 3의 배수가 아니지만 5의 배수이면 "Buzz"
#i가 3의 배수도 아니고 5의 배수도 아닌 경우 i를 그대로 출력한다.

#FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어진다. 이때, 이 세 문자열 다음에 올 문자열은?


#입력 : 연속으로 출력된 세 개의 문자열이 하나씩 주어진다. 각 문자열의 길이는 8이하.
#입력이 항상 FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열에 대응됨이 보장된다.

#출력
#연속으로 출력된 세 개의 문자열 다음에 올 문자열을 출력하자. 여러 문자열이 올 수 있는 경우, 아무 거나 하나 출력하자.


for i in range(3,0,-1):
    x=input()
    if x not in ["FizzBuzz","Fizz","Buzz"]:
        n = int(x)+i

if n%15==0:
    print("FizzBuzz")
elif n%3==0:
    print("Fizz")
elif n%5 == 0:
    print("Buzz")
else:
    print(n)