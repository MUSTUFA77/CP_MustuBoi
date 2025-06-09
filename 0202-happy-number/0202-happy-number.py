class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visit = set()

        while n != 1:
            if n in visit:
                return False
            visit.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return True

        