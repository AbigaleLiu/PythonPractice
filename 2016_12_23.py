# _*_ coding:UTF-8 _*_
"""
leetcode 7
整数的反向位数
"""


# class Solution1(object):
#     """
#     方案一：int转换成str，再转换成list，调用list的reverse方法
#     """
#     str_x = ''
#
#     def reverse(self, x):
#         if type(x) is int:
#             if x > 0:
#                 str_x = str(x)
#                 result = self.str_list_str(str_x)
#                 print int(result)
#             elif x < 0:
#                 str_x = str(-x)
#                 result = self.str_list_str(str_x)
#                 print -int(result)
#             else:
#                 print x
#         else:
#             print "wrong type of x\nplease input an integer"
#
#     @staticmethod
#     def str_list_str(str_x):
#         str_xx = ''
#         list_x = []
#         for i in str_x:
#             list_x.append(i)
#         list_x.reverse()
#         for i in list_x:
#             str_xx = str_xx + i
#         return str_xx


# class Solution2(object):
#     """
#     方案二：字符串切片
#     """
#     def reverse(self, x):
#         if type(x) is int:
#             if x > 0:
#                 str_x = str(x)
#                 print int(str_x[::-1])
#             elif x < 0:
#                 str_x = str(-x)
#                 print -int(str_x[::-1])
#             else:
#                 print x
#         else:
#             print "wrong type of x\nplease input an integer"


class Solution3(object):
    """
    方案三：字符串切片进化版，利用abs()
    """
    def reverse(self, x):
        if x == 0:
            return x
        else:
            print str(abs(x))[::-1] * (x/abs(x))
if __name__ == "__main__":
    x = int(raw_input())
    inst = Solution3()
    inst.reverse(x)
