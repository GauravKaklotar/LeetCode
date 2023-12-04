class Solution:
    def largestGoodInteger(self, num: str) -> str:
        i = '9'
        while int(i) >= 0:
            temp = i * 3
            if temp in num: return temp
            newI = int(i)-1
            i = str(newI)
        return ''