def generate_expressions(nums):
    if len(nums) == 1:
        yield str(nums[0])
    else:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for op in ['+', '-', '*', '/']:
                    new_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                    for left in generate_expressions([nums[i]]):
                        for right in generate_expressions([nums[j]]):
                            # Avoid duplicate expressions for commutative operations
                            if op == '/' and abs(float(eval(right))) < 1e-3:
                                continue  # Avoid division by zero
                            expression = f"({left} {op} {right})"
                            new_nums.append(expression)
                            yield from generate_expressions(new_nums)
                            new_nums.pop()

def evaluate_expression(expression, target):
    try:
        return abs(eval(expression) - target) < 1e-6
    except ZeroDivisionError:
        return False

def mathador_solver(numbers, target):
    solutions = []
    res = {}
    for expression in generate_expressions(numbers):
        if evaluate_expression(expression, target):
            solutions.append(expression)
    
    # Print the total number of solutions and the solutions themselves
    print(f"Total number of solutions: {len(solutions)}")
    for solution in solutions:
        score = calculate_score(solution)
        #print(score)
        #f"Solution: {solution} = {target}, score: {score}"
        res[str(solution)] = score
    return res 


def calculate_score(solution):
    score = 0
    d = {'+': 1, '-': 2, '*': 1, '/': 3}
    for char in solution:
        if char in ['+', '-', '*', '/']:
            score += d[char]
    if score == 7:
        score = 13
    return score

# Example usage
numbers = [2, 3, 6, 8, 19]
target = 32
dz = (mathador_solver(numbers, target))
da = dict(sorted(dz.items(), key=lambda x: x[1], reverse=True))

for k, v in da.items():
    print(f"{k} = {target}, score: {v}")


