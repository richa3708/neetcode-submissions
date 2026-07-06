class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            #sort the word -> same anagrams will have identical sorted form
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())