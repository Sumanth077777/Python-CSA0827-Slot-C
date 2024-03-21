def reverse_number(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    reversed_number = int(reversed_str)
    return reversed_number
num = int(input("Enter a number: "))
result = reverse_number(num)
print("Mirror of the number:", result)
