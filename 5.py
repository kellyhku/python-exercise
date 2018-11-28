count1=0
count2=0
L=[1,2,3,4,5,6]
for i in range(len(L)-1):
   if L[i]<L[i+1]:
    count1 +=1
   elif L[i]>L[i+1]:
    count2 +=1
   else:
    count1 +=1
    count2 +=1
if count1 == len(L)-1:
   print 'UP'
elif count2 ==len(L)-1:
   print 'Down'
else:
  print 'WRONG'

