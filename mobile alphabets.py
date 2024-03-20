def letter_combinations(digits):
    if not digits:
        return []
    keypad = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    def backtrack(index, path):
        if index == len(digits):
            combinations.append(''.join(path))
            return
        current_digit = digits[index]
        for letter in keypad[current_digit]:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()
    combinations = []
    backtrack(0, [])
    return combinations
digits=input("Enter the number:")
output = letter_combinations(digits)
print(output)
