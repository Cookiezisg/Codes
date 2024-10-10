class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow_index = 0
        best_weidth = 0
        answer = ''
        the_dict = {}
        for fast_index in range(len(s)):
            if s[fast_index] in the_dict:
                the_dict[s[fast_index]] += 1
            else:
                the_dict[s[fast_index]] = 1

            while max(the_dict.values()) > 1:
                the_dict[s[slow_index]] -= 1
                slow_index += 1


            if fast_index - slow_index + 1 > best_weidth:
                answer = s[slow_index:fast_index+1]
                best_weidth = len(answer)

        return answer

solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))