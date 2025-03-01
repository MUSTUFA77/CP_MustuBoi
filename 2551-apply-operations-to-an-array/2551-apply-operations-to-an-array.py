class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(0,n-1):
            if nums[i] == nums[i + 1] and nums[i]!=0:
                nums[i] = nums[i]*2
                nums[i+1] = 0

        j = 0
        for i in range(n):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums        