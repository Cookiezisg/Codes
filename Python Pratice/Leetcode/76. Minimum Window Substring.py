class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ''

        t_dict = {}
        for i in t:
            if i not in t_dict:
                t_dict[i] = 1
            else:
                t_dict[i] += 1

        fast_index=0
        slow_index=0
        history_width = len(s) + 1
        history_good_fast = 0
        history_good_slow = 0







solution = Solution()
S = "ADOBECODEBANC"
T = "ABC"
print(solution.minWindow(S, T))