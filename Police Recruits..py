x=int(input())
y=[int(i) for i in input().split()]
c=0
p=0
for i in y:
   if i==-1:
       if p>0:
            p -=1
       else:
            c +=1
   else:
        p +=i
print(c)
            
