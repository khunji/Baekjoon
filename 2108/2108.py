#산술평균 : N개의 수들의 합을 N으로 나눈 값
#중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값\
#최빈값 : N개의 수들 중 가장 많이 나타나는 값
#범위 : N개의 수들 중 최댓값과 최솟값의 차이

#첫째 줄에 수의 개수 N(N은 홀수)
#그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4000을 넘지 않는다.


#첫째 줄 : 산술평균(소수점 이하 첫째 자리에서 반올림)
#둘째 줄 : 중앙값
#셋째 줄 : 최빈값 (여러 개 있을 때 최빈값 중 두번째로 작은 값)
#넷째 줄 : 범위

import sys
from collections import Counter # collections 모듈의 Counter 클래스 
#Counter는 사전(dict) 클래스의 하위 클래스로 리스트나 튜플에서 각 데이터가 등장한 횟수를 사전 형식으로 돌려준다.
#Counter 클래스의 most_common 메소드는 등장한 횟수를 내림차순으로 정리한다.
class Statistics:
    

    def __init__(self, arr:list):
        '''데이터 초기화'''
        #1. 데이터 개수 저장
        self.N = len(arr)

        #2. 정렬된 데이터 저장
        self.sorted_arr = sorted(arr)

    #1. 산술 평균
    def calc_avr(self)->int:
        total_sum = sum(self.sorted_arr)
        return round(total_sum/self.N)
    
    #2. 중앙값
    def calc_medium(self)->int:
        return self.sorted_arr[self.N // 2]
    
    #3. 최빈값
    def calc_count(self)->int:

        cnt = Counter(self.sorted_arr)
        most_common_list = cnt.most_common()#내림차순으로 정렬
        #[ (4,3), (3,2), (5,2), (1,1), (2,1) ] 이런식으로 저장됨.
        max_freq = most_common_list[0][1] #가장 많이 등장한 숫자의 횟수

        mode_candidates = [] #최대 빈도수를 가진 항목(값)들을 저장할 리스트

        for num,freq in most_common_list:
            if freq == max_freq:
                mode_candidates.append(num)
            
            else:
                break
        
        if len(mode_candidates) > 1:
            #최빈값이 여러개일 때:두 번째로 값 리턴하기
            mode_candidates.sort()
            return mode_candidates[1]
        else:
            return mode_candidates[0]




    #4. 범위
    def calc_range(self)->int:
        return (self.sorted_arr[-1] - self.sorted_arr[0])
    
    
        
N = int(sys.stdin.readline()) #수의 개수(홀수만 입력)
arr=[]
for _ in range(N):
    arr.append(int(sys.stdin.readline()))

stc = Statistics(arr)

print(stc.calc_avr())
print(stc.calc_medium())
print(stc.calc_count())
print(stc.calc_range())

