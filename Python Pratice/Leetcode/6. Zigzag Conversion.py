class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        else:
            the_list = [''] * numRows
            pointer = 0
            wave_pointer = 0
            length = len(s)
            while pointer < length:
                while pointer < length and wave_pointer < numRows:
                    the_list[wave_pointer] = the_list[wave_pointer] + s[pointer]
                    wave_pointer += 1
                    pointer += 1
                wave_pointer -= 2
                while pointer < length and wave_pointer >= 0:
                    the_list[wave_pointer] = the_list[wave_pointer] + s[pointer]
                    wave_pointer -= 1
                    pointer += 1
                wave_pointer += 2
            the_answer = ''
            for i in the_list:
                the_answer += i
            return the_answer



solution = Solution()
s = "PAYPALISHIRING"
numRows = 3
solution.convert(s, numRows)