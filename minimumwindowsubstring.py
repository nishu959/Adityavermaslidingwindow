s = input()
t = input()
import sys
mx = sys.maxsize 


mp = {}
for i in t:
  if i in mp:
    mp[i]+=1
  else:
    mp[i] =1
    
i =0
j =0
   
count = len(mp)

while(j<len(s)):
  if s[j] in mp:
    mp[s[j]] -=1
    if mp[s[j]]==0:
      count -=1

  if count!=0:
    j += 1
  if count ==0:
    while count==0:
      mx = min(mx,j-i+1)
      if s[i] not in mp:
        mx = min(mx, j-i+1)
      else:
        mp[s[i]]+=1
        if mp[s[i]]<=0:
          mx = min(mx, j-i+1)
        else:
          count += 1
      i += 1
      
    j +=1
        
          
    
          
       
  
print(mx)