def is_happy(n):
    seen = set()
    while n != 1:
        n = sum(int(digit) ** 2 for digit in str(n))
        if n in seen:
            return False
        seen.add(n)
    return True
input_number = 1
result = is_happy(input_number)
if result:
    print(f"Input: n = {input_number}")
    print("Output: True")
    print("Explanation:")
    print("1^2 + 9^2 = 82")
    print("8^2 + 2^2 = 68")
    print("6^2 + 8^2 = 100")
    print("1^2 + 0^2 + 0^2 = 1")
else:
    print(f"Input: n = {input_number}")
    print("Output: False")
