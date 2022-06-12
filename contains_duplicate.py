# noinspection PyPep8Naming
class Solution:
    @staticmethod
    def containsDuplicate(nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)
