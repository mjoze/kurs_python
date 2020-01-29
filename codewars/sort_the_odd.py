"""
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""


def sort_array(source_array):
    new_arr = [] * len(source_array)
    odd = []
    index_odd = []
    for i, j in enumerate(source_array):
        if j % 2 != 0:
            odd.append(j)
            index_odd.append(i)
    odd.sort()
    for i, j in enumerate(odd):
        new_arr.insert(index_odd[i], j)
    even = []
    index_even = []
    for i, j in enumerate(source_array):
        if j % 2 == 0:
            even.append(j)
            index_even.append(i)
    for i, j in enumerate(even):
        new_arr.insert(index_even[i], j)
    return new_arr


"""
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
"""
"""
def sort_array(source_array):

    odds = []
    answer = []
    
    for i in source_array:
        if i % 2 > 0:
            odds.append(i)
            answer.append("X")
            
        else:
            answer.append(i)
            
    odds.sort()
    
    for i in odds:
        x = answer.index("X")
        answer[x] = i
    return answer
"""


# https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python