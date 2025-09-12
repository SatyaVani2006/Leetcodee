class Solution:
    def isHappy(self, n: int) -> bool:
        S1=set()
        while n!=1 and n not in S1:
            S1.add(n)
            n=sum(int(d)**2 for d in str(n))
        return n==1    
        
