def getFirstSingleLetter(userInput):
    firstSingleLetter = ''
    userInputLowerCase = userInput.lower()
    for i in range(len(userInputLowerCase)):
        if userInputLowerCase.count(userInputLowerCase[i]) == 1:
            firstSingleLetter = userInput[i]
            break
    print(firstSingleLetter)

def rearrangeString(userInput):
    letterCounts = {}
    letterList = {}
    userInputLowerCase = userInput.lower()
    for i in range(len(userInputLowerCase)):
        letterCounts.update({ userInputLowerCase[i]: userInputLowerCase.count(userInputLowerCase[i]) })
        if userInputLowerCase[i] in letterList:
            temp = letterList[userInputLowerCase[i]]
            temp.append(userInput[i])
            letterList.update({ userInputLowerCase[i]: temp })
        else:
            letterList.update({ userInputLowerCase[i]: [userInput[i]] })


    for letter in sorted(letterCounts, key=letterCounts.get):
        for i in range(len(letterList[letter])):
            print(letterList[letter][i], end='')

if __name__ == "__main__":
    userInput = input('Please enter a string:\n')
    getFirstSingleLetter(userInput)
    rearrangeString(userInput)
