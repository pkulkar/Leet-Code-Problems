class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        opening=set('([{')
        matches=[('[',']'),('{','}'),('(',')')]
    
        stack=[]
    
        for p in s:
            if p in opening:
                stack.append(p)
            else:
                if len(stack)==0:
                    return False
                q=stack.pop()
                if (q,p) not in matches:
                    return False
        return len(stack)==0
        