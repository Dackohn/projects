from prettytable import PrettyTable

def generate_truth_table(expression):
    variables = extract_variables(expression)
    num_variables = len(variables)

    table = PrettyTable(variables + ['Result'])
    table.align = 'c'

    for i in range(2 ** num_variables):
        row = get_binary_representation(i, num_variables)
        values = [int(bit) for bit in row]
        result = evaluate_expression(expression, variables, values)
        table.add_row(values + [result])

    print(table)

def extract_variables(expression):
    return list(set(char for char in expression if char.isalpha()))

def get_binary_representation(decimal, length):
    binary = bin(decimal)[2:]
    return '0' * (length - len(binary)) + binary

def evaluate_expression(expression, variables, values):
    for var, value in zip(variables, values):
        expression = expression.replace(var, str(value))

    expression = expression.replace(" ", "")
    expression = expression.replace("+", "|")
    expression = expression.replace("*", "&")
    expression = expression.replace("!", "~")  

    result = eval(expression)
    result = 1 if result else 0

    return result

expression = input("Enter a logical expression: ")
generate_truth_table(expression)
