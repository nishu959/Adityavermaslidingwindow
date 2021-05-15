import sys

mx = -1 * sys.maxsize
i = 0
j = 0
n = int(input())
a = list(map(int, input().split()))
k = int(input())
s = 0
while(j< n):
  s = s + a[j]
  if (j-i+1<k):
    j += 1
  elif (j-i+1==k):
    mx = max(mx, s)
    s = s - a[i]
    i += 1
    j += 1

print(mx)