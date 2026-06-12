class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Declaring hashset to avoid the brute force approach
        hashSet=set()

        #lopping through each and every element of the array
        for i in nums:
            #Checking if the element is present in the hashSet then return True
            if i in hashSet:
                return True
            
            #If not present then we are adding that in hashSet
            hashSet.add(i)

        # If it's not there in the hashSet returning False
        return False
        
        