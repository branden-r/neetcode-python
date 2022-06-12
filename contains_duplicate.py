# noinspection PyPep8Naming
class Solution:
    # if the set of numbers has fewer elements than the sequence of numbers, then a duplicate exists
    @staticmethod
    def containsDuplicate(nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)

    # if the set already contains the number, then a duplicate exists
    @staticmethod
    def setContainsDuplicate(nums: list[int]) -> bool:
        s: set[int] = {nums[0]}
        n: int
        for n in nums[1:]:
            if n in s:
                return True
            s.add(n)
        return False

    # in a sorted sequence of numbers, duplicates will be neighbors
    @staticmethod
    def sortContainsDuplicate(nums: list[int]) -> bool:
        nums.sort()
        n1: int
        n2: int
        for n1, n2 in zip(nums, nums[1:]):
            if n1 == n2:
                return True
        return False
