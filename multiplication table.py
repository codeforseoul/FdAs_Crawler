def print_multiplication_table(num):
    a=1
    while a<=num:
        b=1
        while b<=num:
            n=a*b
            print str(a)+"*"+str(b)+"="+str(n)            
            b=b+1
        a=a+1        

print_multiplication_table(2)    


def printa(n):
    i=1
    while i<=n:
        j=1
        while j<=n:
            print str(i)+"*"+str(j)+"="+str(i*j)
            j=j+1
        i=i+1

printa(2)    
