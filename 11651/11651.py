N = int(input()) #N개의 점

number = [] #빈 리스트

for i in range(N):
   [x,y] = map(int,input().split())
   number.append([y,x])

number.sort()

for i in number:
   print(i[1],i[0])