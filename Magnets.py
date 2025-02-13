count=0
t=int(input())
pre=""
for i in range(t):
    current=input()
    if current!=pre:
        count+=1
    pre=current
print(count)
