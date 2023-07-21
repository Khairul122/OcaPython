def is_balanced_bracket(s):
    stack = []
    opening_brackets = {'(', '{', '['}
    closing_brackets = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or stack[-1] != closing_brackets[char]:
                return "NO"
            stack.pop()

    return "YES" if not stack else "NO"

# Contoh penggunaan fungsi
if _name_ == "_main_":
    sample_inputs = [
        "{ [ ( ) ] }",
        "{ [ ( ] ) }",
        "{ ( ( [ ] ) [ ] ) [ ] }"
    ]

    for s in sample_inputs:
        print(f"Input: {s}")
        print(f"Output: {is_balanced_bracket(s)}")