def sumsquare(l):
    odd = sum(x**2 for x in l if x % 2 != 0)
    even = sum(x**2 for x in l if x % 2 == 0)
    return [odd, even]
num_elements = int(input("Enter the number of elements: "))
elements = []
for _ in range(num_elements):
    element = int(input("Enter the element: "))
    elements.append(element)
result = sumsquare(elements)
print("Output:")
print(result)
