"""
Consider arithmethic expressions that may contain 
various paths of grouping symbols such as 
1. Parentheses: "(" and ")"
2. Braces: "{" and "}"
3. Brackets: "[" and "]"

Each opening symbol must match its corresponding closing symbol
For example
1. Correct: ()(()){([()])}
2. Correct: ((()(()){([()])}))
3. Incorrect: ({[ ])}
4. Incorrect: (

"""


        


def matchPairs(expr): 
    leftPairs = "({["
    rightPairs = ")}]"
    
    # define a stack data structure
    stack = []
    for c in expr: 
        if c in leftPairs: 
            stack.append(c)
            print(stack)
        elif c in rightPairs: 
            print(stack)
            # if stack is empty, dont go on to match
            if len(stack) == 0:    # check if the stack is empty
                return False
            # if the top of the stack is not matching the oppening symbol
            if rightPairs.index(c) != leftPairs.index(stack.pop()):
                print(stack)
                return False
            
    return len(stack) == 0  
                


print(matchPairs("{()}[]"))