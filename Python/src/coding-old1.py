import unittest
import math

def two_sum_old(arr: list, sum: int) -> list:
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == sum:
                return [i, j]
    return None


def two_sum(arr: list, sum: int) -> list:
    left, right = 0, len(arr)-1

    # use two pointers approach
    # https://emre.me/coding-patterns/two-pointers/
    while left < right:
        if arr[left] + arr[right] == sum:
            return [left, right]
        elif arr[left] + arr[right] == sum:
            left += 1
        else:
            right -= 1

    return None

class Test(unittest.TestCase):                                                                                                    
    testcases = [                                                                                                                 
        ([2, 7, 11, 15], 9, [0, 1]),                                                                                                           
        ]                                                                                                                         

    def test(self):                                                                                                      
        for arr, sum, expected in self.testcases:                                                                                     
            assert(two_sum(arr, sum) == expected), f"Failed for value: {arr}, {sum}"                                       

if __name__ == "__main__":
    unittest.main()
