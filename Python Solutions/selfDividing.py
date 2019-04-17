class Solution:
    def decision(self,number:int)->bool:
        digits=list()
        n=number
        while n !=0:
            digits.append(n %10)
            n=int(n/10)
        for digit in digits:
            if digit==0:
                return False
            if number%digit !=0:
                return False
        return True
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        answer=[]
        for i in range(left,right+1,1):
            d=Solution.decision(self,i) 
            if d:
                answer.append(i)
        return answer