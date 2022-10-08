class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # while n != 0:
        #     count += 1
        #     n = n&(n-1)
        mask = 1
        i = 0
        while i < 32:
            if mask & n != 0:
                count += 1
            mask <<= 1
            i += 1
        return count
        