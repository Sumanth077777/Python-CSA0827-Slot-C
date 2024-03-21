def addBinary(a, b):
    result = []
    carry = 0
    a = list(a)
    b = list(b)
    while a or b or carry:
        digit_a = int(a.pop()) if a else 0
        digit_b = int(b.pop()) if b else 0
        total = digit_a + digit_b + carry
        carry = total // 2
        digit = total % 2
        result.append(str(digit))
    result = ''.join(result[::-1])
    return result
a = input("Enter the a:")
b = input("Enter the b:")
print("Input:", "a =", a, "b =", b)
print("Output:", addBinary(a, b))
