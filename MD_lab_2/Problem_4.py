def is_palindrome(s):
        return s == s[::-1]

def shortest_palindrome(str):
    for i in range(len(str) - 1, -1, -1):
        if is_palindrome(str[:i + 1]):
            return str[i + 1:][::-1] + str

    return str

input_str = input("Input: ")
result = shortest_palindrome(input_str)
print(result)
