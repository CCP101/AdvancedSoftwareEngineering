# 改进版 与书上不同 更暴力 建议打断点理解
class Solution:
    def strStr(self, haystack: str, needle: str):
        def getNext(p):
            n = len(p)
            next = [-1] * n
            j, k = 0, -1
            while j < n - 1:
                if (k >= 0 and p[j] == p[k]) or k == -1:
                    j += 1
                    k += 1
                    if p[j] == p[k]:
                        next[j] = next[k]
                    else:
                        next[j] = k
                else:
                    k = next[k]
            return next

        n1, n2 = len(haystack), len(needle)
        next = getNext(needle)
        # print(next)
        i, j = 0, 0
        while i < n1 and j < n2:
            print(i, j)
            if haystack[i] == needle[j] or j == -1:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == n2:
            return i - j
        return -1


sol = Solution()
print(sol.strStr("ababaababcb", "ababc"))
