class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name[0] != typed[0] or len(name) > len(typed):
            return False
        
        i, j= 0, 0
        N, M = len(name), len(typed)
        while not(i == N and j == M):
            if (i < N and j < M and name[i] == typed[j]):
                i += 1
                j += 1
            elif (j < M and typed[j] == name[i-1]):
                j += 1
            else:
                return False
        return True