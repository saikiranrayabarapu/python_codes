l={'O':10,'S':9,'A':8,'B':7,'C':6,'D':5}
sub=int(input("enter no of subjects:"))
sum=0
k=0
for i in range(sub):
    grade=input("enter grade:")
    cre=int(input("enter no of credits:"))
    if grade in l:
        sum=sum+(l.get(grade)*cre)
    elif grade=='F':
        print("oops! it seems you should practice more")
        break
    else:
        print("please give some proper grade:")
        break
    k=k+cre
print(sum/k)

