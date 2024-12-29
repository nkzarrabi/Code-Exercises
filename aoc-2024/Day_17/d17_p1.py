def read_input(file_path):
    """Read registers and program from a file."""
    with open(file_path, 'r') as file:
        # Read all lines, stripping whitespace
        lines = [line.strip() for line in file if line.strip()]
    
    # Check that the file has at least 4 valid lines
    if len(lines) < 4:
        raise ValueError("Input file does not contain enough lines to parse registers and program.")

    # Parse the registers
    try:
        register_a = int(lines[0].split(":")[1].strip())
        register_b = int(lines[1].split(":")[1].strip())
        register_c = int(lines[2].split(":")[1].strip())
    except (IndexError, ValueError) as e:
        raise ValueError(f"Error parsing registers: {e}. Please check the input format.")

    # Parse the program
    try:
        program_line = next((line for line in lines if line.startswith("Program:")), None)
        if program_line:
            program = list(map(int, program_line.split(":")[1].strip().split(",")))
        else:
            raise ValueError("Program line missing.")
    except (IndexError, ValueError) as e:
        raise ValueError(f"Error parsing the program: {e}. Please check the input format.")

    return register_a, register_b, register_c, program


def run_program(register_a, register_b, register_c, program):
    """Simulate the 3-bit computer."""
    A, B, C = register_a, register_b, register_c
    ip = 0
    output = []

    def resolve_combo(operand):
        if operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        elif operand < 4:
            return operand
        else:
            raise ValueError("Invalid combo operand")

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else 0

        if opcode == 0:  # adv
            A //= 2 ** resolve_combo(operand)
        elif opcode == 1:  # bxl
            B ^= operand
        elif opcode == 2:  # bst
            B = resolve_combo(operand) % 8
        elif opcode == 3:  # jnz
            if A != 0:
                ip = operand
                continue
        elif opcode == 4:  # bxc
            B ^= C
        elif opcode == 5:  # out
            output.append(resolve_combo(operand) % 8)
        elif opcode == 6:  # bdv
            B = A // (2 ** resolve_combo(operand))
        elif opcode == 7:  # cdv
            C = A // (2 ** resolve_combo(operand))
        else:
            raise ValueError("Invalid opcode")
        
        ip += 2

    return ",".join(map(str, output))


# Main execution
Test = False
filename = 'example.txt' if Test else 'input.txt'

try:
    register_a, register_b, register_c, program = read_input(filename)
    print(f"Register A: {register_a}")
    print(f"Register B: {register_b}")
    print(f"Register C: {register_c}")
    print(f"Program: {program}")
    
    # Run the program and print the result
    result = run_program(register_a, register_b, register_c, program)
    print(f"Output: {result}")
except Exception as e:
    print(f"Error: {e}")