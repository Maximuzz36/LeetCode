class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # Initialize the max and min product trackers and the global max
        maxp = nums[0]  # Current max product
        maxs = nums[0]  # Current min product
        mx = nums[0]    # Global maximum product
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] < 0:
                # Swap maxp and maxs when encountering a negative number
                maxp, maxs = maxs, maxp
            
            # Update maxp and maxs based on the current number
            maxp = max(nums[i], maxp * nums[i])  # Max of the current number or extending the max product
            maxs = min(nums[i], maxs * nums[i])  # Min of the current number or extending the min product
            
            # Update the global max
            mx = max(mx, maxp)
        
        return mx