# бинарный поиск

def binary_search(l, item):
    low = 0
    high = len(l) - 1
    
    
    while low <= high:
        mid = int((low + high) / 2)
        guess = l[mid]
        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


 # рекурсивные функции + разделяй и властвуй

arr = list(range(10))

def sum_arr(x):
    if x == []:
        return 0
    return x[0] + sum_arr(x[1:])

sum_arr(arr)



arr = list(range(100))

def count_arr(x):
    if x == []:
        return 0
    return 1 + count_arr(x[1:])

count_arr(arr)



# мой вариант

arr = list(range(-11, 200, 2))
arr = list(range(100, 1, -2))

def max_value(x):
    
    if len(x) <= 2:
        try:
            return x[0] if x[0] > x[1] else x[1]
        except:
            return('The list is too small to compare')
    maximum_value = max(x[0], x[-1])
    return maximum_value

max_value(arr)



arr = list(range(100, 1, -2))


def max_value(x):
    
    if len(x) <= 2:
        try:
            return x[0] if x[0] > x[1] else x[1]
        except:
            return('The list is too small to compare')
    maximum_value = max(x[1:])
    return maximum_value if x[0] < maximum_value else x[0]

max_value(arr)

