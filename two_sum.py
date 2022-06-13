class Solution:
    # for the first number, we don't need to check for a solution
    # however, we do need to remember its index
    #
    # for a subsequent number x, the number y we need for a solution is equal to the target minus x
    # if we have seen y before, return its index and the current index
    # otherwise, remember the index of the current number
    @staticmethod
    def twoSum(nums: list[int], target: int) -> tuple[int, int]:
        num_to_idx: dict[int, int] = {nums[0]: 0}
        i: int
        n: int
        for i, n in enumerate(nums[1:], 1):
            partner: int = target - n
            if partner in num_to_idx:
                return i, num_to_idx[partner]
            num_to_idx[n] = i
        return -1, -1
