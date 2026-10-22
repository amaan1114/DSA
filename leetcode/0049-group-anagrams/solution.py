# Runtime: 11 ms
# Memory: 22.1 MB

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in words:
                words[key] = []

            words[key].append(word)

        return list(words.values())
                    
            
