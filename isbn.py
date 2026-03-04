
ISBNCode = "12-4569-8910-21-6"


mainList = ISBNCode.split('-')
print(mainList)

resultsString = ''
for digits in mainList:
    resultsString = resultsString + digits

print(resultsString)

digitList = []
for digit in resultsString:
    digitList.append(digit)

print(digitList)

sum = 0
#compute the sum of the digits
for digit in digitList:
    sum += digit