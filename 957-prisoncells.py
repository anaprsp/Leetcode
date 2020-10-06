#This solution works only for N <= 10^6
#time complexity O(N)
#space complexity O(1), because cells.lenght is 8, so currCells.lenght is 8 aswell
# class Solution:
#     def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
#         currCells = cells[:]
#         while N > 0:
#             for i in range(len(cells)):
#                 if i == 0 or i == len(cells)-1:
#                     currCells[i] = 0
#                 elif cells[i-1] == cells[i+1]:
#                     currCells[i] = 1
#                 else:
#                     currCells[i] = 0
#             cells = currCells[:]
#             N -= 1
#         return cells

#For N <= 10^9
#time complexity O(1), because the size of N will vary according to a fixed amount of repetitions (seen[str(cells)] - currN)
#space complexity O(1)
class Solution:
    def prisonAfterNDays(self, cells, N):
        seen = {}
        while N:
            seen.setdefault(str(cells),N)
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1,7)] + [0]
            if str(cells) in seen:
                N %= seen[str(cells)] - N
        return cells
        