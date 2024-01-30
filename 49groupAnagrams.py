from collections import defaultdict

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
    
    def groupAnagrams_bruteforcev2(self, strs):
        res = {}
        for astr in strs:
            countDict = {}
            for s in astr:
                countDict[s] = 1 + countDict.get(s, 0) 
            key = tuple(sorted(countDict.items()))
            if key not in res:
                res[key] = [astr]
            else:
                res[key].append(astr)
        return list(res.values())

    def groupAnagrams(self, strs):
        res = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)
        return list(res.values())
    
    def groupAnagrams_defaultdict(self, strs):
        res = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            res[key].append(s)
        return list(res.values())
    
    def groupAnagrams_unSorted(self, strs):
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c)-ord("a")] += 1
            res[tuple(count)].append(s)
        return list(res.values())

# Testing
#strs = [""] 
    
#strs = ["a"]

strs = ["eat","tea","tan","ate","nat","bat"]

print(Solution().groupAnagrams_bruteforce(strs))

print(Solution().groupAnagrams_bruteforcev2(strs))

print(Solution().groupAnagrams(strs))

print(Solution().groupAnagrams_defaultdict(strs))

print(Solution().groupAnagrams_unSorted(strs))