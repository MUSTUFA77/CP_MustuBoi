class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word)<3:
            return False
        
        vowel=False
        consonant=False

        for i in word:
            if i.isalpha():
                if i.lower() in "aeiou":
                    vowel=True
                else:
                    consonant=True
            elif not i.isdigit():
                return False
            
        return vowel and consonant
