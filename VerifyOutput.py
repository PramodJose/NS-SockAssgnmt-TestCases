import json
import sys

inFileName = sys.argv[1]
refFileName = "expectedOutput.txt"

inFile = open(inFileName, "r")
refFile = open(refFileName, "r")

inLine = inFile.readline()
refLine = refFile.readline()
testCaseNum = 1
passedAll = True

while len(refLine) > 5:
    inDict = json.loads(inLine)
    refDict = json.loads(refLine)

    if inDict != refDict:
        if passedAll:
            print("\nThe program failed for the following test case(s):-")
        passedAll = False
        print(testCaseNum)

    testCaseNum += 1
    inLine = inFile.readline()
    refLine = refFile.readline()

if passedAll:
    print("\nThe program passed all the test cases!!")