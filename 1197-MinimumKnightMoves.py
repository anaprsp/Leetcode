# Time Complexity O(n^2)
# Space Complexity O(n)
import collections
class Solution:
	def minKnightMoves(self, x: int, y: int) -> int:

		memo = {(0,0):0}
		queue = collections.deque([(0,0)])

		def getNext(loc):
			xx, yy = loc
			for dx,dy in [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]:
				nx, ny = xx + dx, yy + dy
				if (nx,ny) in memo: continue
				yield (nx,ny)

		step = 0
		while (x,y) not in memo:
			step += 1
			for _ in range(len(queue)):
				loc = queue.popleft()
				for next_loc in getNext(loc):
					memo[next_loc] = step
					queue.append(next_loc)
		return memo[(x,y)]