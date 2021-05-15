n = int(input())
a = list(map(int, input().split()))
k = int(input())


i =0
j =0
l = []
ans = []
while(j<n):
  if a[j]<0:
    l.append(a[j])
  if (j-i+1 <k):
    j += 1
  elif j-i+1==k:
    if len(l)==0:
      ans.append(0)
    else:
      ans.append(l[0])
      if a[i]==l[0]:
        l.remove(l[0])
    j += 1
    i += 1
    
    
print(ans)

  
      
  