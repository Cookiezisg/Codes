from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        for i in range(len(intervals)):
            for j in range(0, len(intervals)-i-1):
                if intervals[j][0]>intervals[j+1][0]:
                    temp=intervals[j]
                    intervals[j]=intervals[j+1]
                    intervals[j+1]=temp
        i = 0
        while i < len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals[i]=[intervals[i][0],max(intervals[i+1][1],intervals[i][1])]
                del intervals[i+1]
            else:
                i+=1
        return intervals



solution = Solution()
intervals = [[8,10],[2,6],[15,18],[1,3]]
print(solution.merge(intervals))