class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=len)
        smallest = strs[0]

        for i in range(len(smallest)):
            for stri in strs:
                if i == len(stri) or stri[i] != smallest[i]:
                    return smallest[:i]
        
        return smallest