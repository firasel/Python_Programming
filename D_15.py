s = "Programming Hero is the best"
result = " ".join(["".join(reversed(word)) for word in s.split(' ')])
print(result)
