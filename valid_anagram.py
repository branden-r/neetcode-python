from collections import defaultdict


# noinspection PyPep8Naming
class Solution:
    # if the strings are of different lengths, they cannot be anagrams
    # if they are of the same length, we need to think about it
    #
    # create a mapping from character to integer
    # the integer starts at zero
    # every time a character appears in s, increment the corresponding integer
    # every time a character appears in t, decrement the corresponding integer
    # if they are anagrams, then every mapped value will be a zero
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ct: dict[str, int] = defaultdict(lambda: 0)
        c1: str
        c2: str
        for c1, c2 in zip(s, t):
            ct[c1] += 1
            ct[c2] -= 1
        v: int
        return all(v == 0 for v in ct.values())
