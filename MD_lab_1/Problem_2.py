def xnor_operation(value1, value2):
    result = (value1 and value2) or (not value1 and not value2)
    return result

input1 = bool(int(input("Enter the first value (0 or 1): ")))
input2 = bool(int(input("Enter the second1 value (0 or 1): ")))

output = xnor_operation(input1, input2)

print(f"XNOR result: {int(output)}")
