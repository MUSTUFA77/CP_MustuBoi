#User function Template for python3


def calculategcd(A,B):
    if A == 0:
        return B
    return calculategcd(B%A,A)
    
class Solution:
    def lcmAndGcd(self, A , B):
        gcd = calculategcd(A,B)
        lcm = (A*B)//gcd
        return [lcm,gcd]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends