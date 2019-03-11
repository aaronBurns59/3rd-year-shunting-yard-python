#Aaron Burns
#Shunting Yard Algorithm

def shunt(infix):
    #A dictionary allows setting a higher order of precidences for its items
    #dictionaries are order by strings precidence not an index like an array
    specialSymbols= {'*':50, '.': 40, '|': 30}

    #push and pop operators to this string (push from infix - pop to postfix)
    stack=""
    #return after the infix has been changed to postfix
    postfix=""

    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            #[-1] means the last element in the stack
            while stack[-1] != '(':
                postfix = postfix + stack[-1]
                #sets the stack equal to upto the last character but not including
                #removes last character from stack
                stack= stack[:-1]
            #run again to delete the closing bracket
            stack= stack[:-1]
        #is the character in the dictionary
        elif c in specialSymbols:

        else:
            postfix = postfix + c


    return postfix
