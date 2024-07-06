"""
The Longest Palindromic Subsequence (LPS) (最長回文部分列)

Find the longest palindromic subsequence of a string.
"""


def lps(s):
    if not s:
        return 0
    if len(s) == 1:
        return 1
    if s[0] == s[-1]:
        return 2 + lps(s[1:-1])
    remove_first = lps(s[1:])
    remove_last = lps(s[:-1])

    return max(remove_first, remove_last)


S = "ELRMENMET"
print(lps(S))
