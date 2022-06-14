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
        groups: dict[frozenset[tuple[str, int]], list[str]] = defaultdict(list)
        string: str
        for string in strings:
            groups[frozenset(Counter(string).items())].append(string)
        return list(groups.values())

    # same as above, but without importing collections
    @staticmethod
    def noCollectionsGroupAnagrams(strings: list[str]) -> list[list[str]]:
        groups: dict[frozenset[tuple[str, int]], list[str]] = {}
        string: str
        for string in strings:
            counter: dict[str, int] = {}
            char: str
            for char in string:
                counter[char] = counter.get(char, 0) + 1
            # noinspection PyTypeChecker
            # py type checker thinks this is a frozen set of strings
            # it isn't
            key: frozenset[tuple[str, int]] = frozenset(counter.items())
            groups[key] = groups.get(key, [])
            groups[key].append(string)
        return list(groups.values())
