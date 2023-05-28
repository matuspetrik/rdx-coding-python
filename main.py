"""
The Goal:
Write a program in Python that counts backwards from value provided by user to 1 and prints:
“Agile” if the number is divisible by 5,
“Software” if the number is divisible by 3,
“Testing” if the number is divisible by both, or prints just the number if none of those cases are true.

The script will:
- Print "Testing" only if ALL numbers from isDivisibleBy list are divisors.
- Print "Agile" or "Software" based on tuple's value in isDivisibleBy list respectively.
- Any number of tuples in isDivisibleBy list can be provided.
"""
from Lib.Divisible import IsDivisible as isdivis

def readUserInput():
    while True:
        try:
            data = int(input("Provide a number: "))
        except Exception as inst:
            print("Value is not integer. Try again.")
            continue
        else:
            print("Thank You!")
            break
    return data

def countBackwards(inputInt, divList):
    divisible = isdivis(divList)
    inputInt += 1
    while True:
        inputInt -= 1
        if inputInt == 0:
            break

        # MORE SOPHISTICATED SOLUTION:
        retVal = divisible.byAll(inputInt)
        if retVal:
            print(f"{ inputInt }: { retVal }")
            continue
        retVal = divisible.byOne(inputInt)
        if retVal:
            print(f"{ inputInt }: { retVal }")
        else:
            print(f"{ inputInt }")

        # # SIMPLE SOLUTION:
        # if inputInt % 3 == 0 and inputInt % 5 == 0:
        #     print(f"{ inputInt } Testing")
        # elif inputInt % 5 == 0:
        #     print(f"{ inputInt } Agile")
        # elif inputInt % 3 == 0:
        #     print(f"{ inputInt } Software")
        # else:
        #     print(f"{ inputInt }")

def main():
    readVal = readUserInput()
    isDivisibleBy = [
        (3, "Software"),
        (5, "Agile")
    ]
    countBackwards(readVal, isDivisibleBy)

if __name__ == "__main__":
    main()