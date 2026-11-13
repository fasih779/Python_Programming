class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]

        lenght = 0
        while nums[l] > nums[r]:
            lenght += 1
            l += 1

        return nums[lenght]