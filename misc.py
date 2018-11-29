# Determines if there are any repeated values
# (includes cells with 0 value)
def hasUniqueNumbers(groupedNumbers):
    seen = set()
    for item in groupedNumbers:
        if not item in seen:
            seen.add(item)
        else:
            return False

    return True

# Finds the missing number in a list of
# sequential numbers
def findMissingNumber(sequenceOfNumbers):
    trueSum = int((len(sequenceOfNumbers) * (len(sequenceOfNumbers) + 1)) / 2)
    tot = sum(sequenceOfNumbers)
    return int((trueSum - tot))