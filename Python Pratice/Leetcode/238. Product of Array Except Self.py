from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_nums = 0
        total_time = 1
        zero_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_index.append(i)
                zero_nums += 1
            else:
                total_time = total_time * nums[i]

        if zero_nums == 0:
            for i in range(len(nums)):
                nums[i] = int(total_time / nums[i])
            return nums
        if zero_nums == 1:
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = 0
                else:
                    nums[i] = total_time
            return nums
        if zero_nums > 1:
            return [0] * len(nums)




solution = Solution()
nums = [-1,1,-3,3]
print(solution.productExceptSelf(nums))