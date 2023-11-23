class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        n, m = len(nums), len(l)
        for i in range(m):
            temp = nums[l[i]:r[i]+1]
            length = r[i] - l[i] + 1
            if length >= 2:
                temp.sort()
                diff = temp[1]-temp[0]
                flag = True
                for j in range(1, len(temp)):
                    if temp[j] - temp[j-1] != diff:
                        flag = False
                        ans.append(False)
                        break
                if flag == True: ans.append(True)
            else: ans.append(True)
        return ans            