"""
The Longest Common Subsequence (LCS) (最長共通部分列)

Find the longest common subsequence of two strings.

"""


def lcs(s1, s2):
    if not s1 or not s2:
        return 0
    if s1[-1] == s2[-1]:
        return 1 + lcs(s1[:-1], s2[:-1])

    # NOTE: we shorten the strings from the end because we don't need to pass index to the recursive function
    shorten_s1 = lcs(s1[:-1], s2)
    shorten_s2 = lcs(s1, s2[:-1])

    return max(shorten_s1, shorten_s2)


S1 = "elephant"
S2 = "eretpat"

print(lcs(S1, S2))  # 5
