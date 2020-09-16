class Solution:
    #time complexity O(n^2)
    #space complexity O(n)
    def rotateString(self, A: str, B: str) -> bool:
        if len(B) != len(A):
            return False
        for _ in range(len(A)):
            if A == B:
                return True
            A = A[1:] + A[0]
        return A == ""
        