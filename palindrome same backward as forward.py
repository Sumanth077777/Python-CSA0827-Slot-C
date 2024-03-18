def is_palindrome(x):
    if isinstance(x, int):
        if x < 0:
            return False
        else:
            return str(x) == str(x)[::-1]
    else:
        return False
test_cases = [0]
for case in test_cases:
    print(f"Input: {case}")
    print(f"Output: {is_palindrome(case)}")
