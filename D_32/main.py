days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
rainfall = []
for item in days:
    val = float(input(f"Enter the {item} rainfall amount: "))
    rainfall.append(val)


def mean(data):
    mean = sum(data) / len(data)
    return mean


def variance(data):
    n = len(data)
    mean = sum(data) / n
    deviations = [(x - mean) ** 2 for x in data]
    variance = sum(deviations) / n
    return variance


def deviation(data):
    import math
    var = variance(data)
    std_dev = math.sqrt(var)
    return std_dev


print(f'Mean is {mean(rainfall)}')
print(f'Standard Deviation is {deviation(rainfall)}')
