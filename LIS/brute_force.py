'''
Brute Force Approach: For brute force approach, we can generate all possible subsequences
                      and checking all of them to see if that subsequence is strictly
                      increasing or not. We are also keeping a track of the length of
                      the subsequence if it is strictly increasing to find out the maximum
                      length from them.
                      Time Complexity: O(n * 2^n) - Generating subsequences (2^n), finding maximum length subsequence (O(n))
                      Space Complexity: O(2 ^ n) - storing all possible subsequences
'''


def isIncreasing(seq):
    for i in range(1, len(seq)):
        if seq[i] <= seq[i-1]:
            return False
    return True


def generate(arr):
    result = [[]]
    for num in arr:
        temp = [seq + [num] for seq in result]
        result.extend(temp)
    return result


def findLISLength(arr):
    subsequences = generate(arr)
    result = 0
    for subSeq in subsequences:
        if isIncreasing(subSeq) and len(subSeq) > result:
            result = len(subSeq)
    return result


arr = [11, 5, 2, 5, 3, 7, 101, 18]
print(findLISLength(arr))

