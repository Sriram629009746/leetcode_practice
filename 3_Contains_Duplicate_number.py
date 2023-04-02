class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
		# Brute force: For every element, compare with every other element O(n^2)
		# 1. Sorting(NLogN) + Traverse(N) => NLogN time , O(1) space
		# 2. Hashmap : O(N) time and space
        hmap = {}
        for x in nums:
            if(x in hmap):
                return True
            else:
                hmap[x] = 1

        return False