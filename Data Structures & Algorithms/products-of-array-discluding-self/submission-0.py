class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_of_nums = [1] * n
        
        # Step 1 - Prefix products
        prefix = 1
        for i in range(n):
            product_of_nums[i] = prefix
            prefix *= nums[i]

        # Step2: Suffix products
        suffix = 1
        for i in range(n-1, -1, -1):
            product_of_nums[i] *= suffix
            suffix *= nums[i]

        return product_of_nums
                    

        