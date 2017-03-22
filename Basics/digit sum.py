# 1234 gives 1+2+3+4 i.e., 10
def digit_sum(n):
    b=str(n)
    sum=0
    i=len(b)
    while(i):
        sum=sum+int(b[i-1])
        i=i-1
    print sum
    return 
digit_sum(1234)
