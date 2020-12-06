class Solution:
    #40ms
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = [i for i in nums]
        prev = 0
        for i in nums:
            s = i + prev
            running_sum.append(s)
            prev = prev + i
    
        return running_sum
    
    #32 ms
    def runningSum2(self, nums: List[int]) -> List[int]:
        running_sum = []
        prev = 0
        for i in nums:
            prev += i
            running_sum.append(prev)
    
        return running_sum
    
    
