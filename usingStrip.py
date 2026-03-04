#TYPE STRING
ISBNCode = "12*4569*8910*21*6"

strippedCode = ISBNCode.strip("-")
#If the sum of the digits are divisible by 10 then it is an ISBN Code
def stripCode(code, delimiter):
    resultString = []
    for digit in code:
        if digit == delimiter:
            continue
        resultString.append(int(digit))

    return resultString


def addResult(intergerList): #adds up all digits
    sum = 0
    for i in intergerList:
        sum += i
    return sum



result = stripCode(ISBNCode, '*')
sum = addResult(result)
remainderByTen = sum % 10
print(f'Result {result} sum of list {sum} remainder {remainderByTen}')