def clean_string(text):
    result = ""
    for ch in text:
        if (ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
            result += ch
    return result

s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output = clean_string(s)
print(output)
