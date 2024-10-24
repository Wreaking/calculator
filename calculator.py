# Get user inputs
import math
arithmetic_type = input("Do you want to use Arithmetic Operator (Y/N)?: ").title()

if arithmetic_type in ["Y", "Yes",  "YES", "Yep", "yep", "Yep Operator", "Yup"]:
    operator_type = input("Which Arithmetic Operator do you want to use?: ")
    result_type = input("Do you want the answer in integer form or float form (I/F)?: ").title()
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))
    if operator_type in ["+", "Addition", "Addition Operator", "Add"]:
        if result_type in ["I", "i" ,"Integer", "Integer Form", "Int"]:
            print(num1 + num2)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            print(float(num1) + float(num2))
    elif operator_type in ["-", "Subtraction", "Subtraction Operator", "Subtract"]:
        if result_type in ["I", "Integer", "Integer Form", "Int"]:
            print(num1 - num2)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            print(float(num1) - float(num2))
    elif operator_type in ["*", "Multiplication", "Multiplication Operator", "Multiply"]:
        if result_type in ["I", "Integer", "Integer Form", "Int"]:
            print(num1 * num2)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            print(float(num1) * float(num2))
    elif operator_type in ["/", "Division", "Division Operator", "Divide"]:
        if result_type in ["I", "Integer", "Integer Form", "Int"]:
            print(num1 / num2)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            print(float(num1) / float(num2))
    elif operator_type in ["%", "Modulus", "Modulus Operator", "Mod"]:
        if result_type in ["I", "Integer", "Integer Form", "Int"]:
            print(num1 % num2)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            print(float(num1) % float(num2))
    elif operator_type in ["**", "Exponent", "Exponent Operator", "Exp"]:
        if result_type in ["I", "Integer", "Integer Form", "Int"]:
            print(num1 ** num2)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            print(float(num1) ** float(num2))
    elif operator_type in ["//", "Floor Division", "Floor Division Operator", "Floor Div"]:
        if result_type in ["I", "Integer", "Integer Form", "Int"]:
            print(num1 // num2)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            print(float(num1) // float(num2))
    elif operator_type in ["^", "Power", "Power Operator", "Pow"]:
        if result_type in ["I", "Integer", "Integer Form", "Int"]:
            print(num1 ** num2)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            print(float(num1) ** float(num2))

elif arithmetic_type in ["N", "n", "No", "no", "NO", "Nope", "nope", "Nope"]:
    comparison_type = input("Do you want to use Comparison Operator (Y/N)?: ").title()
    if comparison_type in ["Y", "Yes",  "YES", "Yep", "yep", "Yep Operator", "Yup"]:
        operator_type = input("Which Comparison Operator do you want to use?: ").title()
        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))
        if operator_type in ["==", "Equal", "Equal Operator", "Eq"]:
            if num1 == num2:
                print("True")
            else:
                print("False")
        elif operator_type in [">", "Greater", "Greater Operator", "Gt"]:
            if num1 > num2:
               print("True")
            else:
                print("False")
        elif operator_type in ["<", "Less", "Less Operator", "Lt"]:
            if num1 < num2:
               print("True")
            else:
                print("False")
        elif operator_type in [">=", "Greater Equal", "Greater Equal Operator", "Geq"]:
            if num1 >= num2:
               print("True")
            else:
                print("False")
        elif operator_type in ["<=", "Less Equal", "Less Equal Operator", "Leq"]:
            if num1 <= num2:
                print("True")
            else:
                print("False")
        elif operator_type in ["!=", "Not Equal", "Not Equal Operator", "Neq"]:
            if num1 != num2:
                print("True")
            else:
                print("False")

    elif comparison_type in ["N", "n", "No", "no", "NO", "Nope", "nope", "Nope Operator", "Nope"]:
        trignometry_operator = input("Do you want to use trigonometric expressions (Y/N)?: ").title()
        if trignometry_operator in ["Y", "Yes",  "YES", "Yep", "yep", "Yep Operator", "Yup"]:
            operator_type = input("Which trignometry operator do you want to use?: ")
            num1 = int(input("First Number: "))
            if operator_type in ["sin", "Sin", "Sine", "Sine Operator"]:
                print(math.sin(num1))
            elif operator_type in ["cos", "Cos", "Cosine", "Cosine Operator"]:
                print(math.cos(num1))
            elif operator_type in ["tan", "Tan", "Tangent", "Tangent Operator"]:
                print(math.tan(num1))
            elif operator_type in ["asin", "Asin", "Arcsin", "Arcsin Operator"]:
                print(math.asin(num1))
            elif operator_type in ["acos", "Acos", "Arccos", "Arccos Operator"]:
                print(math.acos(num1))
            elif operator_type in ["atan", "Atan", "Arctan", "Arctan Operator"]:
                print(math.atan(num1))
            elif operator_type in ["asinh", "Asinh", "Arcsinh", "Arcsinh Operator"]:
                print(math.asinh(num1))
            elif operator_type in ["acosh", "Acosh", "Arccosh", "Arccosh Operator"]:
                print(math.acosh(num1))
            elif operator_type in ["atanh", "Atanh", "Arctanh", "Arctanh Operator"]:
                print(math.atanh(num1))

        elif trignometry_operator in ["N", "n", "No", "no", "NO", "Nope", "nope", "Nope Operator", "Nope"]:
            print("Then why are you using the calculator ( -.-)")
            exit()

