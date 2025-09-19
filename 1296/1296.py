English_name = input() #연두의 영어 이름
N = int(input())    #팀 이름의 개수

team_name = N*[0]   #[0,0,0...]-->N개, 팀의 이름을 저장할 리스트

for i in range(N):
    team_name[i]=input()    #team_name에 이름이 저장됨

highest_team=''
highest=-1
team_name.sort()    #내림차순으로 정리-->사전 순으로 정리

for i in range(N):
    score = English_name+team_name[i]
    L_count = score.count('L')
    O_count = score.count('O')
    V_count = score.count('V')
    E_count = score.count('E')
    total = ((L_count+O_count) * (L_count+V_count) * (L_count+E_count) * (O_count+V_count) * (O_count+E_count) * (V_count+E_count)) % 100
    if total > highest:
        highest = total 
        highest_team=team_name[i]
print(highest_team)
        

