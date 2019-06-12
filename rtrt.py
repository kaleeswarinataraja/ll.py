a1,a2=input().split()
temp=0
if len(x1)>len(x2):
  a1,a2=a2,a1
i=0
while i<len(x1):
  temp+=(ord(a2[i])-ord(a1[i]))
  i+=1
for i in range(i,len(a2)):
  temp+=ord(a2[i])-ord('l')+1
print(temp)
