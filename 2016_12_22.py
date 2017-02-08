# _*_ coding:utf-8 _*_
"""
leetcode 1
给定一个列表和整数，返回列表中相加和为给定数的元素序列号
"""


class Solution(object):
    def twoSum(self, nums, target):
        next_num = 1  # 下标增量
        for index in range(len(nums)):
            if self.get_sum(nums[index], nums[index+next_num]) != target:
                next_num += 1
            else:
                print index, index+next_num
            index += 1
        # self.twoSum(nums, target)

    def get_sum(self, num1, num2):
        return num1 + num2
inst = Solution()
inst.twoSum([1, 2, 3], 4)


