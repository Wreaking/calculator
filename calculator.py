#NOTE: we will be using functions and loops to minimize the size of the script soon!

from prettytable import PrettyTable
import math

print("=" * 50)
print(" " * 8 + "Welcome to the Enhanced Calculator!" + " " * 8)
print(" " * 14 + "This calculator supports:"+ " " * 14)
print(" " * 15 + "Arithmetic Operations"+ " " * 15)
print(" " * 15 + "Comparison Operations"+ " " * 15)
print(" " * 14 + "Trigonometric Functions"+ " " * 14)
print("=" * 50)

arithmetic_type = input("Do you want to use Arithmetic Operator (Y/N)?: ").title()

if arithmetic_type in ["Y", "Yes", "YES", "Yep", "yep", "Yep Operator", "Yup"]:
    operator_type = input("Which Arithmetic Operator do you want to use?: ").title()
    result_type = input("Do you want the answer in integer form or float form (I/F)?: ").title()
    num1 = int(input("First Number: "))
    num2 = int(input("Second Number: "))

    if operator_type in ["+", "Addition", "Addition Operator", "Add"]:
        if result_type in ["I", "i", "Integer", "Integer Form", "Int"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Addition", f"{num1}", f"{num2}", f"{num1} + {num2}", num1 + num2])
            print(table)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Addition", f"{num1}", f"{num2}", f"{num1} + {num2}", float(num1 + num2)])
            print(table)
        else:
            print("Invalid result type, Try again later :)")
            exit()

    elif operator_type in ["-", "Subtraction", "Subtraction Operator", "Subtract"]:
        if result_type in ["I", "i", "Integer", "Integer Form", "Int"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Subtraction", f"{num1}", f"{num2}", f"{num1} - {num2}", num1 - num2])
            print(table)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Subtraction", f"{num1}", f"{num2}", f"{num1} - {num2}", float(num1 - num2)])
            print(table)
        else:
            print("Invalid result type, Try again later :)")
            exit()

    elif operator_type in ["*", "Multiplication", "Multiplication Operator", "Multiply"]:
        if result_type in ["I", "i", "Integer", "Integer Form", "Int"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Multiplication", f"{num1}", f"{num2}", f"{num1} * {num2}", num1 * num2])
            print(table)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Multiplication", f"{num1}", f"{num2}", f"{num1} * {num2}", float(num1 * num2)])
            print(table)
        else:
            print("Invalid result type, Try again later :)")
            exit()

    elif operator_type in ["/", "Division", "Division Operator", "Divide"]:
        if num2 != 0:
            if result_type in ["I", "i", "Integer", "Integer Form", "Int"]:
                table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
                table.add_row(["Division", f"{num1}", f"{num2}", f"{num1} // {num2}", num1 // num2])  # Integer division
                print(table)
            elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
                table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
                table.add_row(["Division", f"{num1}", f"{num2}", f"{num1} / {num2}", float(num1 / num2)])
                print(table)
            else:
                print("Invalid result type, Try again later :)")
                exit()
        else:
            print("Undefined (division by zero)")

    elif operator_type in ["%", "Modulus", "Modulus Operator", "Mod"]:
        if result_type in ["I", "i", "Integer", "Integer Form", "Int"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Modulus", f"{num1}", f"{num2}", f"{num1} % {num2}", num1 % num2])
            print(table)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Modulus", f"{num1}", f"{num2}", f"{num1} % {num2}", float(num1 % num2)])
            print(table)
        else:
            print("Invalid result type, Try again later :)")
            exit()

    elif operator_type in ["**", "Exponent", "Exponent Operator", "Exp"]:
        if result_type in ["I", "i", "Integer", "Integer Form", "Int"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Exponent", f"{num1}", f"{num2}", f"{num1} ** {num2}", num1 ** num2])
            print(table)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Exponent", f"{num1}", f"{num2}", f"{num1} ** {num2}", float(num1 ** num2)])
            print(table)
        else:
            print("Invalid result type, Try again later :)")
            exit()

    elif operator_type in ["//", "Floor Division", "Floor Division Operator", "Floor Div"]:
        if result_type in ["I", "i", "Integer", "Integer Form", "Int"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Floor Division", f"{num1}", f"{num2}", f"{num1} // {num2}", num1 // num2])
            print(table)
        elif result_type in ["F", "f", "Float", "Float Form", "Float"]:
            table = PrettyTable(["Arithmetic Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Floor Division", f"{num1}", f"{num2}", f"{num1} // {num2}", float(num1 // num2)])
            print(table)
        else:
            print("Invalid result type, Try again later :)")
            exit()

    else:
        print("Invalid operator, Try again later :)")
        exit()

elif arithmetic_type in ["N", "n", "No", "no", "NO", "Nope", "nope"]:
    comparison_type = input("Do you want to use Comparison Operator (Y/N)?: ").title()
    if comparison_type in ["Y", "Yes", "YES", "Yep", "yep", "Yep Operator", "Yup"]:
        operator_type = input("Which Comparison Operator do you want to use?: ").title()

        num1 = int(input("First Number: "))
        num2 = int(input("Second Number: "))

        if operator_type in ["==", "Equal", "Equal Operator", "Eq"]:
            result = "True" if num1 == num2 else "False"
            table = PrettyTable(["Comparison Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Equal Operator", f"{num1}", f"{num2}", f"{num1} == {num2}", result])
            print(table)

        elif operator_type in [">", "Greater", "Greater Operator", "Gt"]:
            result = "True" if num1 > num2 else "False"
            table = PrettyTable(["Comparison Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Greater Operator", f"{num1}", f"{num2}", f"{num1} > {num2}", result])
            print(table)

        elif operator_type in ["<", "Less", "Less Operator", "Lt"]:
            result = "True" if num1 < num2 else "False"
            table = PrettyTable(["Comparison Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Less Operator", f"{num1}", f"{num2}", f"{num1} < {num2}", result])
            print(table)

        elif operator_type in [">=", "Greater Equal", "Greater Equal Operator", "Geq"]:
            result = "True" if num1 >= num2 else "False"
            table = PrettyTable(["Comparison Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Greater Equal Operator", f"{num1}", f"{num2}", f"{num1} >= {num2}", result])
            print(table)

        elif operator_type in ["<=", "Less Equal", "Less Equal Operator", "Leq"]:
            result = "True" if num1 <= num2 else "False"
            table = PrettyTable(["Comparison Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Less Equal Operator", f"{num1}", f"{num2}", f"{num1} <= {num2}", result])
            print(table)

        elif operator_type in ["!=", "Not Equal", "Not Equal Operator", "Neq"]:
            result = "True" if num1 != num2 else "False"
            table = PrettyTable(["Comparison Operator", "First Number", "Second Number", "Solving", "Result"])
            table.add_row(["Not Equal Operator", f"{num1}", f"{num2}", f"{num1} != {num2}", result])
            print(table)

        else:
            print("Invalid operator, Try again later :)")
            exit()

    elif comparison_type in ["N", "n", "No", "no", "NO", "Nope", "nope"]:
        trigonometry_operator = input("Do you want to use trigonometric expressions (Y/N)?: ").title()
        if trigonometry_operator in ["Y", "Yes", "YES", "Yep", "yep", "Yep Operator", "Yup"]:
            operator_type = input("Which trigonometric operator do you want to use?: ").title()
            num1 = float(input("Angle (in degrees): "))
            angle_rad = math.radians(num1)

            if operator_type in ["Sin", "Sine", "Sine Operator"]:
                table = PrettyTable(["Trigonometric Operator", "Angle (degrees)", "Result"])
                table.add_row(["Sin(ϴ)", f"{num1}", math.sin(angle_rad)])
                print(table)

            elif operator_type in ["Cos", "Cosine", "Cosine Operator"]:
                table = PrettyTable(["Trigonometric Operator", "Angle (degrees)", "Result"])
                table.add_row(["Cos(ϴ)", f"{num1}", math.cos(angle_rad)])
                print(table)

            elif operator_type in ["Tan", "Tangent", "Tangent Operator"]:
                table = PrettyTable(["Trigonometric Operator", "Angle (degrees)", "Result"])
                table.add_row(["Tan(ϴ)", f"{num1}", math.tan(angle_rad)])
                print(table)

            elif operator_type in ["Tanh", "Tanh Operator"]:
                table = PrettyTable(["Trigonometric Operator", "Angle (degrees)", "Result"])
                table.add_row(["Tanh(ϴ)", f"{num1}", math.tanh(angle_rad)])
                print(table)

            elif operator_type in ["Sinh", "Sine Hyperbolic", "Sine Hyperbolic Operator"]:
                table = PrettyTable(["Trigonometric Operator", "Angle (degrees)", "Result"])
                table.add_row(["Sinh(ϴ)", f"{num1}", math.sinh(angle_rad)])
                print(table)

            elif operator_type in ["Cosh", "Cosine Hyperbolic", "Cosine Hyperbolic Operator"]:
                table = PrettyTable(["Trigonometric Operator", "Angle (degrees)", "Result"])
                table.add_row(["Cosh(ϴ)", f"{num1}", math.cosh(angle_rad)])
                print(table)

            else:
                print("Invalid operator, Try again later :)")
                exit()

        elif trigonometry_operator in ["N", "n", "No", "no", "NO", "Nope", "nope"]:
            print("Then why are you using the calculator ( -.-)?")
            exit()

        else:
            print("Invalid input, Try again later :)")

else:
    print("Invalid input, Try again later :)")
