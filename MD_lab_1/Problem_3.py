def get_smaller_permutations(number):
    str_number = str(number)
    length = len(str_number)
    permutations = set()

    generate_permutations("", str_number, permutations, length)

    result = [int(perm) for perm in permutations if int(perm) < number]

    result.sort()

    return result

def generate_permutations(prefix, remaining, permutations, length):
    if len(prefix) == length:
        permutations.add(prefix)
        return

    for i in range(len(remaining)):
        next_digit = remaining[i]
        new_prefix = prefix + next_digit
        new_remaining = remaining[:i] + remaining[i+1:]
        generate_permutations(new_prefix, new_remaining, permutations, length)


input_number = int(input("Enter a number: "))
result = get_smaller_permutations(input_number)
print("Number with the same digits and smaller than", input_number, "is:", result[-1])
