class Solution(object):
    def twoSum(self, nums, target):
        eNums = enumerate(nums)
        sortedNums = sorted(eNums, key = lambda t:t[1])
        
        start, end = 0, len(sortedNums)-1
        
        while start!=end:
            res = sortedNums[start][1] + sortedNums[end][1]
            if res == target:
                return [sortedNums[start][0], sortedNums[end][0]]
            elif res > target:
                end -= 1
            else:
                start += 1