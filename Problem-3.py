a=int(input())
if(a%2==0):
    a=a-1
start=1
for i in range(a):
    if(i!=a-1):
        #comma is not added for the last iteration
        print(start,end=', ')
    else:
        print(start)
    start+=2