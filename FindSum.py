class Solution:
#    def twoSum(self, nums: List[int], target: int) -> List[int]:
    def findSum(self, num, target):
        for index, value in enumerate(nums):
            if target - value in nums:
                print(index, nums.index(target - value))
                return [index, nums.index(target - value)]

if __name__ == '__main__':
    a = [0,1,2,3,4,5,6,7,8,9]
#if __name__ == '__main__':
    print('Hello World')
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 9
    solution = Solution()
    solution.findSum(nums, target)