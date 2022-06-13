from collections import defaultdict
from itertools import groupby


# create a sequence containing a zero for every lowercase letter of the english alphabet
# increment this number every time we see that letter
# create a comma-separated string of these values to use as a key
def string_key(string: str) -> str:
    char_counts: list[int] = [0] * 26
    char: str
    for char in string:
        char_counts[ord(char) - ord("a")] += 1
    return ",".join(str(char_count) for char_count in char_counts)


# noinspection PyTypeChecker
# py type checker is saying that this should return frozenset[str]
# which it never does
#
# create a mapping from character to integer
# this integer begins at zero and is incremented every time we see the corresponding character
# the mapping is implemented with a dictionary, which is unhashable because it is mutable
# to fix this, convert the items in the dictionary to a frozen set, which is hashable because it is immutable
def cold_key(string: str) -> frozenset[tuple[str, int]]:
    char_counts: dict[str, int] = defaultdict(lambda: 0)
    char: str
    for char in string:
        char_counts[char] += 1
    return frozenset(char_counts.items())


# noinspection PyPep8Naming
class Solution:
    # create a mapping from string => key => anagrams
    # the key must be the same for anagrams, and must be hashable
    # return a list of lists of anagrams
    @staticmethod
    def groupAnagrams(strings: list[str]) -> list[list[str]]:
        key_to_group: dict[frozenset[tuple[str, int]], list[str]] = defaultdict(list)
        string: str
        for string in strings:
            key_to_group[cold_key(string)].append(string)
        return list(key_to_group.values())

    # sort the strings by their sorted representation
    # this sorts the anagrams into contiguous groups
    # put every group into its own list
    @staticmethod
    def oneLinerGroupAnagrams(strings: list[str]) -> list[list[str]]:
        # mypy complains about the groupby call due to a bug
        # https://github.com/python/mypy/issues/9920
        return [list(group) for key, group in groupby(sorted(strings, key=sorted), sorted)]  # type: ignore
