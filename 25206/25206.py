#전공평점이 3.3이상이거나 졸업고사를 통과해야 
#졸업고사 응시(x)
#전공평점 계산해주는 프로그램 작성
#전공평점은 전공과목별(학점*과목평점)의 합을 학점의 총합으로 나눈 값
#P/F 과목의 경우 등급이 P 또는 F로 표시되는데, 등급이 P인 과목은 계산에서 제외해야 한다.
#입력 : 20줄에 걸쳐 치훈이가 수강한 전공과목의 과목명, 학점, 등급이 공백으로 구분되어 주어진다.
#출력 : 치훈이의 전공평점을 출력한다. 정답과의 절대오차 또는 상대오차가 0.0001이하이면 정답으로 인정한다.

#제한
#1 ≤ 과목명의 길이 ≤ 50
#과목명은 알파벳 대소문자 또는 숫자로만 이루어져 있으며, 띄어쓰기 없이 주어진다. 입력으로 주어지는 모든 과목명은 서로 다르다.
#학점은 1.0,2.0,3.0,4.0중 하나이다.
#등급은 A+,A0,B+,B0,C+,C0,D+,D0,F,P중 하나이다.
#적어도 한 과목은 등급이 P가 아님이 보장된다.

sum=0
sum_credit=0

for i in range(20):
    name,credit,grade = input().split()
    if grade=='A+':
        sum+=float(credit)*4.5
        sum_credit+=float(credit)
    elif grade=='A0':
        sum+=float(credit)*4.0
        sum_credit+=float(credit)
    elif grade=='B+':
        sum+=float(credit)*3.5
        sum_credit+=float(credit)
    elif grade=='B0':
        sum+=float(credit)*3.0
        sum_credit+=float(credit)
    elif grade=='C+':
        sum+=float(credit)*2.5
        sum_credit+=float(credit)
    elif grade=='C0':
        sum+=float(credit)*2.0
        sum_credit+=float(credit)
    elif grade=='D+':
        sum+=float(credit)*1.5
        sum_credit+=float(credit)
    elif grade=='D0':
        sum+=float(credit)*1.0
        sum_credit+=float(credit)
    elif grade=='P':
        pass
    else:
        sum+=float(credit)*0.0
        sum_credit+=float(credit)

print(format(sum/sum_credit, ".6f"))