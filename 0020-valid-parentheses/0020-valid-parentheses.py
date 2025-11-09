class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_match = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in valid_match.values():
                stack.append(i)
            elif i in valid_match.keys():
                if not stack or stack.pop() != valid_match[i]:
                    return False 

        return not stack

        
        