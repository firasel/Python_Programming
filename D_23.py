exStr = "We tried list and we tried dicts also we tried Zen"


def countWord(wordArr):
    wordDict = {}
    for word in wordArr:
        if word in wordDict.keys():
            wordDict[word] = wordDict[word]+1
        else:
            wordDict[word] = 1
    return wordDict


wordArr = exStr.split(' ')
wordDict = countWord(wordArr)
for key, val in wordDict.items():
    print(f'{key}\t{val}')
