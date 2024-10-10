from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_value = 0
        left_pointer = 0
        right_pointer = len(height)-1
        while left_pointer < right_pointer:
            current_area = min(height[left_pointer],height[right_pointer]) * (right_pointer-left_pointer)
            max_value = max(max_value,current_area)
            
            if height[left_pointer]<height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_value


solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))