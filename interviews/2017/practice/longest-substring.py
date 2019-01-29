import math


"""
def lengthOfLongestSubstring(input):
    if not len(input):
        return 0

    max_substring = input[0]
    for charIndex in range(len(input)):
        s = set()
        temp_substring = ""
        for substringCharIndex in range(charIndex, len(input)):
            testChar = input[substringCharIndex]
            if testChar in s:
                temp_substring = input[charIndex:substringCharIndex]
                break
            s.add(testChar)

        if len(max_substring) < len(temp_substring):
            max_substring = temp_substring

    return max_substring

print(lengthOfLongestSubstring("abcabc"))
print(lengthOfLongestSubstring("bbbb"))
print(lengthOfLongestSubstring("bwwkew"))


"""





def longestIncreasingSubsequence(input):
    if not input:
        return input


    longestFound = 0
    longestSubsequenceIndex = 0

    LONGEST_AT_POINT = [None] * len(input)
    PREV = [None] * len(input)

    # For each point, find the longest subsequence until this point
    # Track the "prev" value at each point
    for i in range(0, len(input)):
        LONGEST_AT_POINT[i] = 1
        PREV[i] = None
        current_item = input[i]

        for j in range(0, i):
            # Any time the path is less than or equal, and it's a viable subsequence, update
            if input[j] <= current_item and LONGEST_AT_POINT[j] >= LONGEST_AT_POINT[i]:
                LONGEST_AT_POINT[i] = LONGEST_AT_POINT[j] + 1
                PREV[i] = j

        if longestFound < LONGEST_AT_POINT[i]:
            # New max found
            longestFound = LONGEST_AT_POINT[i]
            longestSubsequenceIndex = i


    # Build sequence from prev
    built_subsequence = []
    idx = longestSubsequenceIndex
    for i in range(longestFound):
        built_subsequence = [ input[idx] ] + built_subsequence
        idx = PREV[idx]


    return built_subsequence

print(longestIncreasingSubsequence([1,2,5,5,5,5,3,3,4,5]))

