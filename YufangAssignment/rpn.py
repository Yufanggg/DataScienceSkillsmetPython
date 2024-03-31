import sys

def rpn(tokens):

    OperNum = {
        "+": tokens.count("+"),
        "-": tokens.count("-"),
        "*": tokens.count("*"),
        "/": tokens.count("/")
        }
    
    while len(tokens) >2:
        if sum(OperNum.values()) == 0:
            RuntimeError("Not enough operators; too many elements on remained on stack.")
        else:
            for Oper, Num in OperNum.items():
                if Num == 0:
                    continue
                else: 
                    for i in range(Num):
                        # print(f"Num = {Num}")
                        curOper = Oper
                        curOperLoc = tokens.index(curOper)
                        # print(curOperLoc)
                        NewItem = eval(''.join(str(x) for x in [tokens[curOperLoc-2], curOper, tokens[curOperLoc-1]]))
                        # print(NewItem)
                        tokens.insert(curOperLoc-2, NewItem)
                        # print(tokens)
                        tokens.pop(curOperLoc+1)
                        # print(tokens)
                        tokens.pop(curOperLoc)
                        # print(tokens)
                        tokens.pop(curOperLoc-1)
                        # print(tokens)
                        Num = Num -1
                        # print(f"Num = {Num}")
    if len(tokens) == 2:
        if sum(OperNum.values()) == 0:
            raise RuntimeError("Not enough operators; too many elements on remained on stack.")
        elif sum(OperNum.values()) == 1:
            # print("yes")
            Oper = [key for key, value in OperNum.items() if value == 1][0]
            # print(Oper)
            raise RuntimeError("Not enough arguments for {} operators". format(Oper))

    if len(tokens) == 1:
        
        if isinstance(tokens[0], str):
            raise ValueError(f"could not convert string to float: {tokens[0]}")
        else:
            return(tokens[0])
        
if __name__ == "__main__": 
    args = sys.argv[1:]
    args = [int(arg) if arg.isdigit() else float(arg) if "." in arg else arg for arg in args]
    # print(args)
    # print(type(args))
    Output = float(rpn(args))
    print(f"{Output}")
