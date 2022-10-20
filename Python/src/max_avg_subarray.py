import unittest
import math

def max_average_subarray_old(arr: list, k: int) -> float:
    n = len(arr)
    max_avg_val = float('-inf')

    for i in range(n-k+1):
        _sum = 0
        for j in range(i, i+k):
            _sum += arr[j]
        max_avg_val = max(max_avg_val, _sum/k)
        
    return max_avg_val

def max_average_subarray(arr: list, k: int) -> float:
    n = len(arr)
    average = []
    _sum = start = 0

    # use a sliding window approach
    # https://emre.me/coding-patterns/sliding-window/
    for end in range(n):
        _sum += arr[end] # add the next element
        if end >= k - 1: # we've collected k items now
            average.append(_sum / k)
            # slide the window
            _sum -= arr[start]
            start += 1

    return max(average)

class Test(unittest.TestCase):                                                                                                    
    testcases = [                                                                                                                 
        ([1, 12, -5, -6, 50, 3], 4, 12.75),                                                                                                           
        ]                                                                                                                         

    def test(self):                                                                                                      
        for arr, k, expected in self.testcases:                                                                                     
            assert(max_average_subarray(arr, k) == expected), f"Failed for value: {arr}, {k}"                                       

if __name__ == "__main__":
    unittest.main()
