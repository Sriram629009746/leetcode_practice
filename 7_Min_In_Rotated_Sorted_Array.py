class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        
        
        while(left < right):

            mid = int((left+right)/2)

            if(left == mid):
                if(nums[left]>nums[right]):
                    return nums[right]
                else:
                    return nums[left]

            if(nums[mid]>nums[right]):
                left = mid
            else:
                right = mid

        return nums[left]
