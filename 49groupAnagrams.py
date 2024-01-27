class Solution:
    def groupAnagrams_bruteforce(self, strs):
        res = []
        dictList = []
        for astr in strs:
            countDict = {}
            for s in astr:
                countDict[s] = 1 + countDict.get(s, 0) 
            if countDict not in dictList:
                dictList.append(countDict)
                res.append([])
            for i, n in enumerate(dictList):
                if n == countDict:
                    res[i].append(astr)
        return res

# Testing
strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams(strs))