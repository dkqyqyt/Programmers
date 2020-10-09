import math
def solution(w,h):
    g = gcd(w,h)

    if w >= h:
        small = h
        big = w
        it = h//g

    else:
        small = w
        big = h
        it = w//g

    cut = 0
    for i in range(it):
        start = (big*i)//small
        end = (big*(i+1))//small
        if (big*(i+1))%small == 0:
            cut += end-start
        else:
            cut += end-start+1
    print(cut)
    return w*h - cut*g

def gcd(m,n):
    if m < n:
        m,n = n,m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)

w = 8
h = 12
print(solution(w,h))