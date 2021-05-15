import sys
n = int(input())
a = list(map(int, input().split()))
k = int(input())

i = 0
j = 0
s = 0
mx =0

while(j<n):
  s = s+ a[j]
  if s<k:
    j=j +1
  elif s == k:
    mx = max(mx, j-i+1)
    j = j + 1
  elif s>k:
    while(s>k):
      s = s-a[i]
      i = i +1
    j = j +1
    
    
print(mx)
    
  
  