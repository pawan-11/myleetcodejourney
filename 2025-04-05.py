class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        answer = []
        mncost = cost[0]
        for i in range(len(cost)):
            mncost = min(mncost, cost[i])
            answer.append(mncost)
        return answer
