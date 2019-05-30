num=int(input("enter num:"))
l=[]
for i in range(1,10000):
    if(num%i==0):
        if(i==num):
            break
        l.append(i)
sum=0
for j in l:
    sum=sum+j
if(num==sum):
    print("it is a perfect number")
else:
    print("it is not a perfect number")
