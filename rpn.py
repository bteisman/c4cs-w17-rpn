#!/usr/bin/env python3

import readline
import operator


operators = {
	"+":operator.add,
	"-":operator.sub,
	"^":operator.pow,
	"*":operator.mul,
	"/":operator.truediv,
}

def calculate(arg):
	stack = []
	for operand in arg.split():
		try:
			num = float(operand)
			stack.append(num)
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			stack.append(operators[operand](arg1, arg2))

	return stack.pop()		

def main():
    while True:
        result = calculate(input("rpn calc> "))
        print(result)
        
if __name__ == '__main__':
    main()