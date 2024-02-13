#1
def countdown(num):
    countdown_list = []
    for i in range(num, -1, -1):
        countdown_list.append(i)
    return countdown_list
print(countdown(5))
#2
def print_and_return(nums):
    print(nums[0])
    return nums[1]
print(print_and_return([1,2]))
#3
def first_plus_length(lst):
    sum = lst[0] + len(lst)
    return sum
print(first_plus_length([1,2,3,4,5]))
#4
def values_greater_than_second(values):
    if len(values) < 2:
        return False
    greater_values = []
    for i in values:
        if i > values[1]:
            greater_values.append(i)
    print(len(greater_values))
    return greater_values
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))
#5
def length_and_value(size, value):
    return [value] * size
print(length_and_value(4,7))
print(length_and_value(6,2))