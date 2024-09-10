class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                nums[a] = nums[i]
                a +=1
        return a
        