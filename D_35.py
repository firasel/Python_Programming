data = [{'a': 5, 'b': 10}, {'x': 15, 'y': 20}]
for val in range(len(data)):
    for key, val2 in data[val].items():
        print(f"Key:{key} Value:{val2}")
