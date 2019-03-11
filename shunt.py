def shunt(infix):
    #A dictionary allows setting a higher order of precidences for its items
    #dictionaries are order by strings precidence not an index like an array
    specials= {'*':50, '.': 40, '|': 30}

    #return after the infix has been changed to postfix
    postfix=''
    #push and pop operators to this string (push from infix - pop to postfix)
    stack=''

    for c in infix:
        if c == '(':
            stack = stack + c
        elif c == ')':
            #[-1] means the last element in the stack
            while stack[-1] != '(':
                postfix, stack = postfix + stack[-1], stack[:-1]
                #sets the stack equal to upto the last character but not including
                #removes last character from stack
            #run again to delete the closing bracket
            stack= stack[:-1]
        #is the character in the dictionary
        elif c in specials:
        #once you've read a special character
            while stack and specials.get(c, 0) <= specials.get(stack[-1],0):
                postfix, stack = postfix + stack[-1], stack[:-1]
            #puts the special character on the stack
            stack = stack + c
        else:
            postfix = postfix + c
        #anything thats at the end of the stack is added to the postfix and removed from the stack
    while stack:
        #postfix = postfix + stack[-1]
        #stack= stack[:-1]
        #can do all in one line
        postfix, stack = postfix + stack[-1], stack[:-1]
    return postfix
print(shunt("(a.b)|(c*.d)"))
