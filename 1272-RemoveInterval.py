# Time Complexity O(len(intervals))
# SpaceComplexity O(len(intervals))
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        
        a = toBeRemoved[0]
        b = toBeRemoved[1]
        
        newList = []
        
        for i in intervals:
            if i[0] < a:
                if i[1] <= a:
                    newList.append(i)
                elif i[1] > a and i[1] <= b:
                    newList.append([i[0],a])
                elif i[1] > b:
                    newList.append([i[0],a])
                    newList.append([b,i[1]])
                
            elif i[0] >= a and i[0] < b:
                if i[1] > a and i[1] <= b:
                    continue
                else:
                    newList.append([b,i[1]]) 
                    
            elif i[0] >= b:
                newList.append(i)
                
        return newList
        