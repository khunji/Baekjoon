while True:
    a = list(map(int,input().split()))
    if (a[0] and a[1] and a[2]) == 0:
        break
    max_a = max(a)
    a.remove(max_a)
    if a[0]**2+a[1]**2==max_a**2:
        print('right')
    else:
        print('wrong')
