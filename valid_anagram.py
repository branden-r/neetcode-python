# noinspection PyPep8Naming
# create a mapping from each unique character in the string to the number of times it occurs
def charCount(s: str) -> dict[str, int]:
    r: dict[str, int] = {}
    c: str
    for c in s:
        if c not in r:
            r[c] = 1
        else:
            r[c] += 1
    return r


# noinspection PyPep8Naming
class Solution:
    # if the two strings have an equal mapping, they are anagrams
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        return charCount(s) == charCount(t)
