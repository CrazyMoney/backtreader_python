# #最长的回文
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         n = len(s)
#         dp = [[False] * n for _ in range(n)]
#         ans = ""
#         # 枚举子串的长度 l+1
#         for l in range(n):
#             # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
#             for i in range(n):
#                 j = i + l
#                 if j >= len(s):
#                     break
#                 if l == 0:
#                     dp[i][j] = True
#                 elif l == 1:
#                     dp[i][j] = (s[i] == s[j])
#                 else:
#                     dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
#                 if dp[i][j] and l + 1 > len(ans):
#                     ans = s[i:j+1]
#         return ans

#
# def longestPalindrome( s):
#     """
#     :type s: str
#     :rtype: str
#     """
#     star_num = 0
#     end_num = 0
#     star_str = ''
#     if len(s) <= 1:
#         return s
#     for i in range(len(s)):
#         star_str = s[i]
#         for j in range(i, len(s)):
#             if s[j] == star_str and j-i  >= end_num-star_num:
#                 star_num, end_num = i, j
#     return s[star_num:end_num + 1]
#
#
#
# l = 'aba'
# ans = longestPalindrome(l)
# print(ans)

# def convert( s, numRows):
# #     """
# #     :type s: str
# #     :type numRows: int
# #     :rtype: str
# #     """
# #
# #     colume_num, row_num = numRows, numRows - 2  # 每个循环的字符数量
# #     group_num = 0
# #     start_num = 0
# #     z_cloume = 0
# #     z_row = 0
# #     for i in range(len(s)):
# #         group_num = int(i % (colume_num + row_num))
# #         start_num = start_num + group_num + 1
# #         mid_num = start_num + colume_num
# #         end_num = start_num + colume_num + row_num
# #         if i >= start_num and i < mid_num:#处于列上的字符
# #             print( s[i] + '\n')
# #         else: #处于斜线的字符
# #             print())
# # s = "LEETCODEISHIRING"
# # convert(s,3)

#
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if numRows < 2: return s
#         res = ["" for _ in range(numRows)]
#         i, flag = 0, -1
#         for c in s:
#             res[i] += c
#             if i == 0 or i == numRows - 1: flag = -flag
#             i += flag
#         return "".join(res)
# s =  Solution()
# l = "LEETCODEISHIRING"
# rees  = s.convert(l,3)
# print( rees)


class Foo(object):
    def __init__(self):
        pass

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """

        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """

        # printThird() outputs "third". Do not change or remove this line.
        printThird()
from multiprocessing import  Process
import queue
q =  queue.Queue(3)




