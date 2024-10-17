'''
Binary Search Approach: We can also utilize binary search approach along with dynamic programming
                        to improve the complexities. We store smallest element for the subsequence
                        at each index. Then utilize binary search to find the position of each elements.
                        It will improve both the time complexity and the space complexity.
                        Time Complexity: O(n log n)
                        Space Complexity: O(n) storing smallest element at each index
'''


def findLISLength(arr):
    if not arr: return 0
    smallest = [0] * len(arr)
    result = 0
    for num in arr:
        left, right = 0, result
        while left < right:
            mid = (left + right) // 2
            if smallest[mid] < num:
                left = mid + 1
            else:
                right = mid
        smallest[left] = num
        result = max(result, left+1)
    return result


arr = [11, 5, 2, 5, 3, 7, 101, 18]
print(findLISLength(arr))

