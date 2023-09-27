class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        
        # Calculate the total size of the decoded string
        for char in s:
            if char.isdigit():
                size *= int(char)
            else:
                size += 1
        
        # Iterate through the string in reverse to find the kth character
        for char in reversed(s):
            k %= size
            if k == 0 and char.isalpha():
                return char
            
            if char.isdigit():
                size //= int(char)
            else:
                size -= 1

        return ""
