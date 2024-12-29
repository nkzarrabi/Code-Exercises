import re
from z3 import BitVec, Optimize, sat


class ClassicVM:
    def __init__(self, a, b, c, inst):
        self.a, self.b, self.c, self.inst = a, b, c, inst
        self.ip = 0

    def combo(self, label):
        return {4: self.a, 5: self.b, 6: self.c}.get(label, label)

    def adv(self, operand):
        self.a >>= self.combo(operand)

    def bxl(self, operand):
        self.b ^= operand

    def bst(self, operand):
        self.b = self.combo(operand) & 0x07

    def bxc(self, operand):
        self.b ^= self.c

    def bdv(self, operand):
        self.b = self.a >> self.combo(operand)

    def cdv(self, operand):
        self.c = self.a >> self.combo(operand)

    def jnz(self, operand):
        if self.a != 0:
            self.ip = operand - 2

    def out(self, operand):
        print(self.combo(operand) & 0x07, end=",")

    def run(self):
        while self.ip < len(self.inst):
            opcode, operand = self.inst[self.ip], self.inst[self.ip + 1]
            {
                0: self.adv,
                1: self.bxl,
                2: self.bst,
                3: self.jnz,
                4: self.bxc,
                5: self.out,
                6: self.bdv,
                7: self.cdv,
            }[opcode](operand)
            self.ip += 2


class SymbolicVM(ClassicVM):
    def __init__(self, a, b, c, inst):
        super().__init__(a, b, c, inst)
        self.osolver = Optimize()
        self.a = BitVec("a", 128)  # Symbolic representation of `a`
        self.constraints_cnt = 0

    def jnz(self, operand):
        if self.constraints_cnt == len(self.inst):
            self.osolver.add(self.a == 0)
            raise StopIteration  # Stop execution once constraints are done
        self.ip = operand - 2

    def out(self, operand):
        if self.constraints_cnt < len(self.inst):
            # Add constraint to match output to program
            self.osolver.add(self.combo(operand) & 0x07 == self.inst[self.constraints_cnt])
            self.constraints_cnt += 1

    def run(self):
        start_a = self.a
        try:
            super().run()
        except StopIteration:
            # Minimize `a` and solve constraints
            self.osolver.minimize(start_a)
            if self.osolver.check() == sat:
                print(self.osolver.model()[start_a])


def task1(input_data: str):
    a, b, c, *inst = map(int, re.findall(r"-?\d+", input_data))
    vm = ClassicVM(a, b, c, inst)
    vm.run()


def task2(input_data: str):
    a, b, c, *inst = map(int, re.findall(r"-?\d+", input_data))
    vm = SymbolicVM(a, b, c, inst)
    vm.run()


if __name__ == "__main__":
    import sys

    # Choose Task 1 or Task 2 based on the input
    mode = sys.argv[1] if len(sys.argv) > 1 else "task2"
    filename = sys.argv[2] if len(sys.argv) > 2 else "input.txt"

    with open(filename, "r") as file:
        input_data = file.read().strip()

    if mode == "task1":
        task1(input_data)
    elif mode == "task2":
        task2(input_data)
    else:
        print("Invalid mode! Use 'task1' or 'task2'.")