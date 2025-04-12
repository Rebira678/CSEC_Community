class Solution:
    def sortColors(self, nums: List[int]) -> None:
        if not nums:
            return

        max_val = max(nums)
        count = [0] * (max_val + 1)

        for i in nums:
            count[i] += 1
        
        index = 0
        for j in range(len(count)):
            for _ in range(count[j]):
                nums[index] = j
                index += 1
