class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        last = {}

        for i, x in enumerate(s):
            last[x] = i
        
        stack = []
        visited = set()

        for i in range(len(s)):
            if s[i] in visited:
                continue
            
            while stack and stack[-1] > s[i] and last.get(stack[-1], -1) > i:
                visited.remove(stack.pop())
            
            visited.add(s[i])
            stack.append(s[i])
        
        return ''.join(stack)