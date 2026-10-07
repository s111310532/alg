import sys
sys.setrecursionlimit(2000)

def my_map(fn, seq):
    if not seq:
        return []
    return [fn(seq[0])] + my_map(fn, seq[1:])

def my_filter(predicate, seq):
    if not seq:
        return []
    head, tail = seq[0], seq[1:]
    rest = my_filter(predicate, tail)
    return [head] + rest if predicate(head) else rest

def my_reduce(fn, acc, seq):
    if not seq:
        return acc
    return my_reduce(fn, fn(acc, seq[0]), seq[1:])

def bubble_step(acc, val):
    sorted_prefix, current_max = acc
    if current_max > val:
        return sorted_prefix + [val], current_max
    return sorted_prefix + [current_max], val

def bubble_pass(arr):
    if len(arr) <= 1:
        return arr
    prefix, max_val = my_reduce(bubble_step, ([], arr[0]), arr[1:])
    return prefix + [max_val]

def bubble_sort(arr, passes=None):
    if passes is None:
        passes = len(arr)
    if passes <= 1 or len(arr) <= 1:
        return arr
    return bubble_sort(bubble_pass(arr), passes - 1)

data = [64, 34, 25, 12, 22, 11, 90, 5]
print(bubble_sort(data))
