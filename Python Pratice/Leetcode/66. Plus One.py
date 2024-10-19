from typing import List
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        the_last_num = 1
        for i in range(len(digits)-1,-1,-1):
            the_last_num = the_last_num + digits[i]
            digits[i] = the_last_num % 10
            the_last_num = int((the_last_num - the_last_num % 10) / 10)
            if the_last_num == 0:
                break
        
        if the_last_num == 0:
            return digits
        else:
            return [the_last_num] + digits


solution = Solution()
digits = [9,9,9]
print(solution.plusOne(digits))