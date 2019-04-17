class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        answer=list(list())
        for row in A:
            ans=[]
            for i in reversed(range(len(row))):
                ans.append(row[i])
            for i in range(len(ans)):
                if ans[i]==0:
                    ans[i]=1
                else:
                    ans[i]=0
            answer.append(ans)
        return answer
            