class Solution:
    def hash_anagram(self, s: str) -> tuple:
        freq_list = 26 * [0]

        for c in s:
            alphabet_idx = ord(c) - ord('a')
            freq_list[alphabet_idx] += 1
        
        key = tuple(freq_list)

        return key

    def insert(self, string, key, dict):
        if key in dict:
            dict[key].append(string)
        else:
            dict[key] = [string]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_dict = {}

        for s in strs:
            hash = self.hash_anagram(s)
            self.insert(s, hash, anagrams_dict)
        
        return list(anagrams_dict.values())