n = int(input())
a = list(map(int, input().split()))
k = int(input())

i= 0
j = 0
ans = []
l = []

while(j< n):
  while(len(l)>0 and a[j]>l[-1]):
    l.pop()
  l.append(a[j])
  if (j-i+1<k):
    j += 1
  elif (j-i+1==k):
    ans.append(l[0])
    if l[0]==a[i]:
      l.pop(0)
    i += 1
    j += 1
   
  
print(ans)