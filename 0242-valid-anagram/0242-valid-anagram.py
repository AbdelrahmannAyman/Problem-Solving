class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        sm = {}
        tm = {}
        for ch in s:
            if ch in sm:
                sm[ch] += 1
            else:
                sm[ch] = 1

        for ch in t:
            if ch in tm:
                tm[ch] += 1
            else:
                tm[ch] = 1

        for k, v in tm.items():
            if k not in sm:
                return False
            elif tm[k] != sm[k]:
                return False
        return True