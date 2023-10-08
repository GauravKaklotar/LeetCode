class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        memo = {}

        def solve(i, j, l1, l2, l):
            if i == n1 or j == n2:
                if l == 1:
                    return 0
                else:
                    return -1
            elif (i, j, l) in memo:
                return memo[(i, j, l)]
            else:
                op1 = l1[i] * l2[j] + solve(i+1, j+1, l1, l2, 1)
                op2 = solve(i+1, j, l1, l2, l)
                op3 = solve(i, j+1, l1, l2, l)
                memo[(i,j,l)] = max(op1, op2, op3)
                return memo[(i,j,l)]
        
        ans = solve(0, 0, tuple(nums1), tuple(nums2), 0)
        if ans == -1:
            nums1.sort()
            nums2.sort()
            return max(nums1[0] * nums2[-1], nums1[-1] * nums2[0])
        else:
            return ans



# class Solution:
#     def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
#         n1, n2 = len(nums1), len(nums2)
#         memo = [[[-float('inf') for _ in range(2)] for _ in range(n2)] for _ in range(n1)]

#         def solve(i, j, l1, l2, l):
#             if i == n1 or j == n2:
#                 if l == 1:
#                     return 0
#                 else:
#                     return -1
#             elif memo[i][j][l] != -float('inf'):
#                 return memo[i][j][l]
#             else:
#                 op1 = l1[i] * l2[j] + solve(i+1, j+1, l1, l2, 1)
#                 op2 = solve(i+1, j, l1, l2, l)
#                 op3 = solve(i, j+1, l1, l2, l)
#                 memo[i][j][l] = max(op1, op2, op3)
#                 return memo[i][j][l]
        
#         ans = solve(0, 0, tuple(nums1), tuple(nums2), 0)
#         if ans == -1:
#             nums1.sort()
#             nums2.sort()
#             return max(nums1[0] * nums2[-1], nums1[-1] * nums2[0])
#         else:
#             return ans
