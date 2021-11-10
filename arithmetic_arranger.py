def arithmetic_arranger(problems, answer=False):
    ''' breakingdown the problems '''
    left = [x.split()[0] for x in problems]
    operators = [x.split()[1] for x in problems]
    right = [x.split()[2] for x in problems]
    numbers = set(left + right)

    ''' error handling  '''
    if len(problems) > 5:
        return "Error: Too many problems."
    elif any(x not in {"+", "-"} for x in set(operators)):
        return "Error: Operator must be '+' or '-'."
    elif [s for s in numbers if not s.isdigit()]:
        return "Error: Numbers must only contain digits."
    elif [s for s in numbers if len(s) > 4]:
        return "Error: Numbers cannot be more than four digits."

    ''' formatting '''
    arranged_problems = ''
    dash_count = [len(max(x.split(), key=len))+2 for x in problems]
    print(dash_count)
    arranged_problems += "    ".join([(dash_count[c] - len(i))
                                     * ' ' + i for c, i in enumerate(left)])+"\n" + "    ".join([operators[c] + (dash_count[c] - len(i) - 1)
                                                                                                 * ' ' + i for c, i in enumerate(right)])+'\n' + "    ".join([i * '-' for i in dash_count])

    if answer:
        arranged_problems += "\n"+"    ".join([(dash_count[c] - len(i))
                                               * ' ' + i for c, i in enumerate([str(eval(p)) for p in problems])])

    # print(repr(arranged_problems))
    # print()
    return arranged_problems


arithmetic_arranger(['3801 - 2', '123 + 49'])


# '  3801      123\n-    2    +  49\n------    -----'
# '  3801     123\n-    2    + 49\n------    ----'
