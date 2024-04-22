lm=[]
count=0
result=0
max=0

def list_maghsoom():
    n=num//2
    for i in range(1,n+1):
        if num%i==0:
            lm.append(num//i)
    return(lm)

def tedad_aval():
    c=0

    n2=item
    for i in range(1,n2+1):
        if n2%i==0:
            c+=1

    return(c)
    
        


for i in range (1,11):
    num=int(input())
    list_maghsoom()
    for item in lm:
        c=tedad_aval()
        if c==2:
            count+=1
    if count>max:
        max=count
        result=num
    elif count==max and num>result:
        result=num
    lm=[]
    count=0

print(result,' ',max)