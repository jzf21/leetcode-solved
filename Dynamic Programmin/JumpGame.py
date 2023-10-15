class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        max_reachable = nums[0]
        steps = 1
        end = nums[0]
        
        for i in range(1, len(nums)):
            if i > end:
                steps += 1
                end = max_reachable
            max_reachable = max(max_reachable, i + nums[i])
        
        return steps
