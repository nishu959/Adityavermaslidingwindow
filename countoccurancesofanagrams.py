a = input()
b = input()

ans =0
m = {}

for i in b:
  if i in m:
    m[i] = m[i] +1
  else:
    m[i] =1
    


i =0
j =0
count = len(m)
k = len(b)

while(j <len(a)):
  if a[j] in m:
    m[a[j]] -= 1
    if m[a[j]] == 0:
      count -= 1
  if (j-i+1 <k):
    j += 1
  elif (j-i+1==k):
    if count==0:
      ans += 1
    if a[i] in m:
      m[a[i]] += 1
      if m[a[i]] == 1:
        count += 1
    i += 1
    j += 1
   
  
print(ans)