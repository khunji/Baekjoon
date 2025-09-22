C=int(input()) #테스트 케이스의 개수


for i in range(C): 
    count=0
    scores = list(map(int,input().split())) # scores[0]는 학생의 수, scores[1:]는 학생의 모든 점수
    average = sum(scores[1:])/scores[0]

    for j in range(1,scores[0]+1):
        if scores[j]>average:
            count+=1
    result=count/scores[0]*100
    print(format(result,".3f")+'%')

        