# from functools import lru_cache
# class Solution:
#     def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:

#         directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
#         n = 10 ** 9
#         @lru_cache(maxsize=None)
#         def solve(i, j, time_left):
#             if i==fx and j==fy: return time_left == 0
#             if i > fx or j > fy or time_left==0: return False

#             for x, y in directions:
#                 new_row, new_col = i + x, j + y

#                 if 1 <= new_row <= n and 1 <= new_col <= n:
#                     if solve(new_row, new_col, time_left-1): return True
#             return False

#         if sx == fx and sy == fy: return True
#         return solve(sx, sy, t) 

class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x_dist = abs(sx - fx)
        y_dist = abs(sy - fy)

        if x_dist == 0 and y_dist == 0:
            return t != 1

        return x_dist <= t and y_dist <= t        