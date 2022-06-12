# noinspection PyPep8Naming
class Solution:
    # if the set of numbers has fewer elements than the sequence of numbers, then a duplicate exists
    @staticmethod
    def containsDuplicate(nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
