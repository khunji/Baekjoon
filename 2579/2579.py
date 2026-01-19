import sys
input = sys.stdin.readline

N = int(input())#계단의 개수

score = [0]*301
for i in range(1,N+1):
    score[i] = int(input())
#무엇을 dp로 정할 것인가?
#dp[i] = i번째 계단을 올랐을 때의 점수의 최댓값
#score[i] = i번째 계단의 점수

#초기식
#dp[1] = score[1]
#dp[2] = score[1] + score[2]
#dp[3] = max(score[1]+score[3],score[2]+score[3])

#점화식
#dp[i] = dp[i-2]+score[i]
#dp[i] = dp[i-3]+score[i]+score[i-1]
#이중에 더 큰거 고르자.

dp=[0]*301
dp[1] = score[1]
dp[2] = score[1]+score[2]
dp[3] = max(score[1]+score[3],score[2]+score[3])

for i in range(4,N+1):
    dp[i] = max(dp[i-2]+score[i], dp[i-3]+score[i-1]+score[i])

print(dp[N])
