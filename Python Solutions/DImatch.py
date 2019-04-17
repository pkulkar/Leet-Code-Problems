class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        answer=list()
        i=0
        N=len(S)
        for s in S:
            if s =='I':
                answer.append(i)
                i+=1
            else:
                answer.append(N)
                N-=1
        answer.append(i)
        return answer