operation_string = input()
operation_string = str(operation_string).strip() # removes any whitespace from the input

def two_stack_algorithm(string):

    values = []
    operators = []

    for char in operation_string:

        if char == "(": # ignores left paranthesis
            pass
        else:
            try:
                char = int(char)
                values.append(char) # integers into the values list
            except:
                if char == ")": # right parantheses initiate operation

                    first_value = values.pop()
                    second_value = values.pop()
                    operator = operators.pop()

                    if operator == "+":
                        result = first_value + second_value
                        values.append(result)
                    elif operator == "-":
                        result = first_value - second_value
                        values.append(result)
                    elif operator == "*":
                        result = first_value * second_value
                        values.append(result)
                    elif operator == "/":
                        result = first_value / second_value
                        values.append(result)

                else: # other characters into the operators list
                    operators.append(char)

    return values[0]

print(two_stack_algorithm(operation_string))
