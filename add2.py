import sys
try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    sum = num1+num2
    print("the result is ", sum)
except ValueError:
    print("Please profer two valid numbers.")
