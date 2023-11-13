class Solution:
    def sortVowels(self, s: str) -> str:
        stack = []

        def check_vowels(c):
            return c in 'aeiouAEIOU'
        
        for c in s:
            if check_vowels(c): stack.append(c)

        if len(stack)==0: return s
        
        stack.sort(reverse=True)

        s = list(s)
        for i in range(len(s)):
            if check_vowels(s[i]):
                temp = stack.pop()
                s[i] = temp
        
        return ''.join(s)
