from functools import reduce

def average(array):
    array = list(set(array))
    total = reduce(lambda x,y: x + y, array)
    avg = total / len(array)
    return avg 