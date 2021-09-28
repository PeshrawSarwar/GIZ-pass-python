

class Solution(object):

    @staticmethod
    def longest_palindromic(s: str):
        # Square Matrix - length = length of the string
        matrix = [[False for i in range(len(s))] for i in range(len(s))]
        for i in range(len(s)):
                matrix[i][i] = True
        max_length = 1
        start = 0
        for l in range(2,len(s)+1):
            for i in range(len(s)-l+1):
                end = i+l
                if l==2:
                    if s[i] == s[end-1]:
                        matrix[i][end-1]=True
                        max_length = l
                        start = i
                else:
                    if s[i] == s[end-1] and matrix[i+1][end-2]:
                        matrix[i][end-1]=True
                        max_length = l
                        start = i
        return s[start:start+max_length]

ob = Solution()
print(ob.longest_palindromic("lagalabcd"))


