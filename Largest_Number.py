class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=self.compare, reverse=True)
        result = ''.join(nums)
        return '0' if result[0] == '0' else result
    
    def compare(self, num1):
        return num1 * 10
