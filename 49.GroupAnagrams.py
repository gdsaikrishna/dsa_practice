class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        return [sorted(g) for _, g in itertools.groupby(sorted(strs, key=sorted), sorted)]