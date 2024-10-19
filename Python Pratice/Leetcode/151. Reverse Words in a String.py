class Solution:
    def reverseWords(self, s: str) -> str:
        dp = []
        word = ""
        for i in s:
            if i == ' ' and word != '':
                dp.append(word)
                word = ''  
            elif i != ' ':
                word = word + i
        if word: 
            dp.append(word)
        
        answer = ''
        for i in range(len(dp) - 1, -1, -1):
            if i != 0:
                answer = answer + dp[i] + ' '
            else:
                answer = answer + dp[i]  
        
        return answer




solution = Solution()
s = "the sky is blue"
print(solution.reverseWords(s))