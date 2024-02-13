#1.
def biggie_size(array):
    for x in range(0,len(array),1):
        if array[x]>0:
            array[x] = 'big'
    return array
print(biggie_size([-1, 3, 5, -5]))
#2.
def count_positives(array):
    count = 0
    for x in array:
        if x>0:
            count += 1
    array[len(array)-1] = count
    return array
print(count_positives([1,1,-2,1]))
#3.
def sum_total(array):
    sum = 0
    for x in array:
        sum += x
    return sum
print(sum_total([1,2,3,4]))
#4.
def average(array):
    sum = 0
    for x in array:
        sum += x
    return (sum/len(array))
print(average([1,2,3,4]))
#5.
def length(array):
    length = 0
    for x in array:
        length = length + 1
    return length
print(length([37,2,1,-9]))
#6.
def minimum(array):
    if len(array)<0:
        return False
    min = array[0]
    for x in array:
        if x<min:
            min = x
    return min
print(minimum([-37,2,1,-9]))
#7.
def maximum(array):
    if len(array)<0:
        return False
    max = array[0]
    for x in array:
        if x>max:
            max = x
    return max
print(maximum([37,2,100,-9]))
#8.
def ultimate_analysis(array):
    dictionary = {'sum':0, 'avg':0, 'min':array[0], 'max':array[0], 'length':0}
    for x in array:
        dictionary['sum'] += x
        dictionary['avg'] += dictionary['sum']/len(array)
        if x < dictionary['min']:
            dictionary['min'] = x
        if x > dictionary['max']:
            dictionary['max'] = x
        dictionary['length'] = dictionary['length'] + 1
    return dictionary
print(ultimate_analysis([37,2,1,-9]))
#9.
def reverse_list(array):
    array.reverse()
    return array
print(reverse_list([37,2,1,-9]))