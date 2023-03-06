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


#Optimised

#User function Template for python3

def printFirstNegativeInteger( A, N, K):
    
    from collections import deque
    l = deque([])
    ans = []
    
    i, j=0,0
    
    
    while j<N:
        
        if A[j]<0:
            l.append(A[j])
            
        if j-i+1<K:
            j += 1
            
        elif j-i+1==K:
            
            if len(l)==0:
                ans.append(0)
            else:
                ans.append(l[0])
                
                if A[i]==l[0]:
                    l.popleft()
            
            i += 1
            j += 1
    return ans
            
            
            
        
    
    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
