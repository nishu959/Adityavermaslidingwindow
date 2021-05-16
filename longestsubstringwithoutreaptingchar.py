import sys

s = input()


i = 0
j =0
mx = -1*sys.maxsize
mp ={}

while(j<len(s)):
  if s[j] in mp:
    mp[s[j]] += 1
  else:
    mp[s[j]] = 1
  
  
  if len(mp)==j-i+1:
    mx = max(mx, j-i+1)
    j+=1
  elif len(mp)<j-i+1:
    while(len(mp)<j-i+1):
      mp[s[i]] -= 1
      if mp[s[i]]==0:
        mp.pop(s[i])
      i+=1
    j+=1
print(mx)