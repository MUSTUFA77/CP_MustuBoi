class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        sorted_arr=sorted(nums)
        for i in range(n):
            if nums[i:]+nums[:i]==sorted_arr:
                return True
        return False
        