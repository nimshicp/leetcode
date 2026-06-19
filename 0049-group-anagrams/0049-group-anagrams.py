class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            key=''.join(sorted(i))
            if key in d:
                d[key].append(i)
            else:
                d[key]=[i]
        return list(d.values())            
        