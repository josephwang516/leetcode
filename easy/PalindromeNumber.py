class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        #edge case negative numbers
        if (x < 0):             
            return False
        
        #convert number to a string
        numberstring = str(x)
        strlth = len(numberstring)

        #if single digit, is palindrome
        if strlth ==1:
            return True

        #create int array from characters
        array = [int (x) for i,x in  enumerate(numberstring)]

        #iterate from 0 to midpoint
        for j in range(0, int(len(array)/2)):
            #if not the same, return false
            if array[j] != array[len(array)-j-1]:
                return False
        #iterated through the whole loop, is true
        return True
          