#User function Template for python3


class Solution:
    def evenlyDivides (self, n):
        
        # code here
        count = 0
        original_n = n
        while n > 0:
            last_digit = n % 10
            n = n // 10
            if last_digit != 0 and original_n % last_digit == 0:
                count += 1
        return count





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends