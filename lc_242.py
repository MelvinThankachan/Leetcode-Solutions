class Solution(object):
    def isAnagram(self, s, t):
        ns = len(s)
        nt = len(t)
        if ns != nt:
            return False
        ds = {}
        dt = {}
        for i in range(ns):
            if s[i] not in ds:
                ds[s[i]] = 1
            else:
                ds[s[i]] += 1
            if t[i] not in dt:
                dt[t[i]] = -1
            else:
                dt[t[i]] -= 1
        for key in ds.keys():
            if key not in dt.keys() or ds[key] != dt[key]:
                return False
        return True
