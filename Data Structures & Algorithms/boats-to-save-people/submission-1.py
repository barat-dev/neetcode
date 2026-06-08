class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        m = max(people)
        count = [0] * (m + 1)

        for p in people:
            count[p] += 1
        
        idx = 0
        i = 1
        while idx < len(people):
            while count[i] == 0:
                i += 1
            
            people[idx] = i
            count[i] -= 1
            idx += 1
        
        l, r = 0, len(people) - 1
        res = 0
        while l<=r:
            if l == r:
                res += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                r -= 1
                l += 1
                res += 1
            else:
                r -= 1
                res += 1
        return res

        