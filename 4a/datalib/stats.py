def mean(data, key):
    # calculamos la media de los valores de la clave dada
    numeros = [float(d[key]) for d in data]
    return sum(numeros) / len(numeros)


def median(data, key):
    nums = sorted([float(d[key]) for d in data])
    n = len(nums)
    mid = n // 2
    if n % 2 == 0:
        return (nums[mid-1] + nums[mid]) / 2
    return nums[mid]
