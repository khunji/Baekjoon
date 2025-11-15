import sys


def solution(a1, a2):

    s = set(a1)
    result = []
    for i in a2:
        result.append("1" if i in s else "0")
    print("\n".join(result))
        

input = sys.stdin.readline
N = int(input())
arr1 = list(map(int, input().split()))
M = int(input())
arr2 = list(map(int,input().split()))
solution(arr1, arr2)
