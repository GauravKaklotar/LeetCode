class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        s_counter, t_counter = Counter(s), Counter(t)
        for key in t_counter.keys():
            if t_counter[key] != s_counter[key]:
                return key
        


        # s, t = list(s), list(t)
        # s.sort()
        # t.sort()
        # for i in range(len(s)):
        #     if t[i] != s[i]:
        #         return t[i]
        # return t[-1]