class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(B) != len(A):
            return False
        i = 0
        while i <= len(A):
            if A == B:
                return True
            A = A[1:] + A[0]
            i += 1  
        return False