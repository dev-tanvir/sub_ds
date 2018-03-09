def parentheses_check_using_stack(input_str):
    s = list()

    for ch in input_str:
        if ch == '(':
            s.append(ch)
        if ch == ')':
            if not s:
                return False
            s.pop()

    return not s


if __name__ == "__main__":
    input_str = input()

    if parentheses_check_using_stack(input_str):
        print(input_str, "is balanced")

    else:
        print(input_str, "is not balanced")