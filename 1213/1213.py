import sys
from collections import Counter

s = sys.stdin.readline().strip() 
n = len(s) 

def palindrome_maker(s):
    
    count = Counter(s)
    sorted_items = sorted(count.items()) 
    
    
    left_half = ""  
    mid_char = ""   
    odd_count = 0   

    
    for char, cnt in sorted_items:
        
        if cnt % 2 != 0:
            odd_count += 1
            mid_char = char

       
        left_half += char * (cnt // 2)

    
    if odd_count > 1:
        return "I'm Sorry Hansoo"
    
    
    
    final_palindrome = left_half + mid_char + left_half[::-1]
    return final_palindrome


if n == 0:
    print("")
else:
    print(palindrome_maker(s))