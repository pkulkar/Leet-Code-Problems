class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        Jewels=list()
        for jewel in J:
            Jewels.append(jewel)
        Stones=list()
        for stone in S:
            Stones.append(stone)
        count=0
        for i in range(len(Stones)):
            if Stones[i] in Jewels:
                count+=1
                
        return count