
import itertools
#start with a list of however numbers
def func(ints: list[int], target: int):
    print('note: order of operations is not considered')
    print('ops are sequential only')
    print('if nothing is printed, assume this is impossible')
    
    # Counter to keep track of the total number of combinations
    total_combinations = 0
    score = 0 
    d = { '+':1 , '-': 2, '*': 1, '/': 3}
    # can solve this recursively
    def helper(acc: int, ints: list[int], ops: list[str], index: int):
        nonlocal total_combinations
        nonlocal score 
        # ints is empty
        if index >= len(ints):
            if abs(acc - target) < 0.0001 :
                # Increment the total_combinations counter
                total_combinations += 1

                # Print here
                print('###################')
                print(ints)
                print(ops)
            return
                
        # ints is not empty
        # in that case, try running the 4 operators +, -, *, /
        head = ints[index]
        
        helper(acc+head, ints, ops + ['+'], index+1)
        helper(acc-head, ints, ops + ['-'], index+1)
        helper(acc*head, ints, ops + ['*'], index+1)
        if head != 0:
            helper(acc/head, ints, ops + ['/'], index+1)
        
    for perm in itertools.permutations(ints):
        head = perm[0]
        helper(head, perm, [], 1)
    
    # Print the total number of combinations at the end
    print(f'Total combinations that lead to the target value: {total_combinations, sc}')

nums = [19, 8, 6, 3, 2]
target = 32

func(nums, target)