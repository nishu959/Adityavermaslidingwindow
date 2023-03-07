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
    
  
  #For negative numbers
  

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        import sys
        m = {}
        s = 0
        mx =0
        m[0] = 0
        #Complete the function
        for i in range(n):
            
            s += arr[i]
            
            
            if s-k in m:
                mx = max(mx, i-m[s-k]+ 1)
            
            
            if s not in m:
                m[s] = i + 1
        
      
        return mx
  
  
