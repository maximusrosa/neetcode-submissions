class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1_count = {}
        c2_count = {}

        for c1, c2 in zip(s, t):
            self.upsert(c1, c1_count)
            self.upsert(c2, c2_count)


        if c1_count == c2_count:
            return True

        
        return False

    def upsert(self, char, dict):
        if char in dict:
            dict[char] += 1
        else:
            dict[char] = 1