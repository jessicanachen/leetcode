class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        containedNums = []
        for num in nums:
            if num in containedNums:
                return True
            containedNums.append(num)
        return False
    
'''
Time Complexity: 
O(n) - We iterate through the list of numbers once, worst case scenario is that all numbers are unique.

Space Complexity:
O(n) - We store the numbers in a list to check for duplicates, worst case scenario is that all numbers are unique.
'''

'''
Alternative Solution:
- you could use a set using hte property that sets do not allow duplicates, just convert the list to a set and compare the lengths
- if the lengths are the same, then there are no duplicates
- if the lengths are different, then there are duplicates
- this solution has a time complexity of O(n) and a space complexity of O(n)
'''

'''
Thought Approach:
- essentially in both solutions, we are checking if a number has been seen before
- the list one approaches this one by doing it systematically
  - we look at each item individually, and we keep track of what we have seen before
  - if we see it again, theres the duplicate
- the set one approaches this by taking advantage of the properties of sets
  - essentially the set checks for the duplicate by creation, thus its like a black box
  - we have a friend we give him stuff and he gives us it back taking out all the duplicates
  - thus, if we have less items than before, there was a duplicate
'''