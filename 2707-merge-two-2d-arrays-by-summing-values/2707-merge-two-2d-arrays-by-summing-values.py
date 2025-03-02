class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        dictionary = defaultdict(int)

        for id_,value in nums1:
            dictionary[id_] += value
        
        for id_,value in nums2:
            dictionary[id_] += value

        return sorted(dictionary.items())