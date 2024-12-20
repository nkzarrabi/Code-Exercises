from itertools import product

def evaluate(numbers, ops):
    """
    Evaluates the numbers with the given operators applied strictly left-to-right.
    """
    val = numbers[0]
    for num, op in zip(numbers[1:], ops):
        if op == '+':
            val += num
        elif op == '*':
            val *= num
        elif op == '||':  # Concatenation operator
            val = int(str(val) + str(num))
    return val


def gen_ops_fast(opcount, part):
    """
    Uses itertools.product to generate all possible operator combinations.
    For Part One: Operators are + and *
    For Part Two: Operators are +, *, and ||
    """
    operators = ['+', '*'] if part == 1 else ['+', '*', '||']
    return product(operators, repeat=opcount)


def calculate_calibration(equations, part):
    """
    Calculates the total calibration result for the specified part (1 or 2).
    """
    calibration = 0
    for equation in equations:
        # Parse the target value and the list of numbers
        value, numbers = equation.split(': ')
        value = int(value)
        numbers = list(map(int, numbers.split(' ')))

        opcount = len(numbers) - 1

        # Iterate through all operator combinations
        for ops in gen_ops_fast(opcount, part):
            result = evaluate(numbers, ops)
            if result == value:
                print(f"Valid equation (Part {part}): {numbers} with ops {ops} = {result}")
                calibration += value
                break

    return calibration


if __name__ == '__main__':
    # Hardcoded input file name
    filename = "input.txt"

    # Read equations from the input file
    with open(filename, 'r') as f:
        equations = f.read().splitlines()

    # Part One
    part_one_result = calculate_calibration(equations, part=1)
    print(f'Total calibration result (Part One): {part_one_result}')

    # Part Two
    part_two_result = calculate_calibration(equations, part=2)
    print(f'Total calibration result (Part Two): {part_two_result}')