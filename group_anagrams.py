from collections import Counter, defaultdict


# noinspection PyPep8Naming
class Solution:
    # create a mapping from anagram to group of anagrams
    # return a list of groups
    #
    # notes:
    # two strings are anagrams iff they have the same number of each character
    @staticmethod
    def groupAnagrams(strings: list[str]) -> list[list[str]]:
        anagram_to_group: dict[frozenset[tuple[str, int]], list[str]] = defaultdict(list)
        string: str
        for string in strings:
            anagram_to_group[frozenset(Counter(string).items())].append(string)
        return list(anagram_to_group.values())
