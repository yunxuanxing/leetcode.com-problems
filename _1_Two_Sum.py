class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 该方法利用两层循环，时间复杂度过高，leetcode的测试最后一项输入数字很多，超时
        # len_nums = len(nums)
        # for x in range(len_nums):
        #     for y in range(len_nums):
        #         if x < y and nums[x] + nums[y] == target:
        #             return [x, y]

        # 以下方法利用字典的哈希表方法，仅一层循环，效率高
        len_nums = len(nums)
        dict_target={}
        for x in range(len_nums):
            dict_target[nums[x]] = x
        # 将第一层循环结果放入字典
        # print(dict_target)   #仅用于debug查看
        for y in range(len_nums):
            complement = target - nums[y]
            if complement in dict_target and dict_target[complement] != y:
                # print([y, dict_target[complement]])
                return [y, dict_target[complement]]
                # 注意：return成功之后循环就结束了，代码不会继续运行了，如果循环中有多个结果均符合要求，也只会return第一次的结果




