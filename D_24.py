def checkPalindrome(sampleStr):
    revStr = ""
    for ch in sampleStr:
        revStr = ch+revStr
    return sampleStr == revStr


sampleStr = "abba"
if checkPalindrome(sampleStr):
    print(f'{sampleStr} is palindrome')
else:
    print(f'{sampleStr} is not palindrome')
