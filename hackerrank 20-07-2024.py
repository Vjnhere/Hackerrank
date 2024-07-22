import sys
import ast

def maxSubArray(nums):
    # Initialize the variables
    max_sum = float('-inf')
    current_sum = 0
    
    # Iterate through the array
    for num in nums:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

if __name__ == '__main__':
    input = sys.stdin.read().strip()
    
    # Extract the list of integers from the input string
    # Assumes input format is 'nums = [...]'
    nums_str = input.split('=')[1].strip()
    nums = ast.literal_eval(nums_str)
    
    # Print the result
    print(maxSubArray(nums))
