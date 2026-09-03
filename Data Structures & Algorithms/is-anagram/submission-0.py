class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for letter in s:
            count[letter] = count.get(letter, 0) + 1

        for letter in t:
            if letter not in count or count[letter] == 0:
                return False
            else:
                count[letter] -= 1
        return True