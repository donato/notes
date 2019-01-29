"""
given a list of daily temperatures produce a list that,
 for each day in the input,
  tells you how many days you would have to wait until a warmer temperature


Input  [ 70, 80, 70, 70, 80]
Output [ 1,  3,  2, 1, None]

Input  [ 70, 75, 70, 70, 80]
       [          2, 1, None]

      Going backwards, if smaller guarantee to start over at 1
                       if same, guaranteed to increment by 1
                       if larger, increment by 1
      At each point, you want the first date that has temp greater than or equal to your temperature
"""


temperatures = [ 5,4,3,4,5,4,3,4,5]

"""
results = []
# O(n^2)
for t in range(len(temperatures)):
    for i in range(t+1, len(temperatures)):
        best_value = None
        if temperatures[t] < temperatures[i]:
            best_value = i - t
            break
    results.append(best_value)

print(results)

"""

results = [None for x in temperatures]

# Stack represents days which haven't found a higher temperature yet
#  Each addition will first remove everything smaller than itself
#     Thus, the days within it will be sorted from largest to smallest
stack = [0]

# Skip first element
for t in range(len(temperatures))[1:]:
    # Keep popping off the stack until you reach a lower temperature than present
    while len(stack) > 0 and temperatures[t] > temperatures[stack[-1]]:
        day_to_update = stack.pop()
        results[day_to_update] = t - day_to_update
    stack.append(t)


print(results)
