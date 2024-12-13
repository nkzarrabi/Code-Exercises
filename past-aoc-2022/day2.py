example_text = '''A Y
B X
C Z'''

print(example_text)

text = {2: open('input2.txt').read()}

#print(text[2])

# Total score is the sum of the scores for each round 
# The score for a single round is the score for the shaep you selected 
# (1 for rock, 2 for paper, and 3 for scissors) plus the score of the outcome of the round (0, if you lost, 3 if draw, 6 if you won)

lines = text[2].splitlines()
#lines = example_text.splitlines()
t = [line.split() for line in lines]

print(t)
# first round 
# first player chooses A, second player chooses Y
# A is rock, B is paper, C is scissors
# Rock beats scissors, so A beats C 
# X is also rock, Y is also paper, Z is also scissors
# A is rock, Y is paper so round 1 
# You chose paper so you beat rock, you get 5 points for winning 
#+ 2 for choosing paper 

def char_to_shape(c):
    if c in ['A', 'X']:
        return 'Rock'
    elif c in ['B', 'Y']:
        return 'Paper'
    elif c in ['C', 'Z']:
        return 'Scissors'
    else:
        return 'Error'

d = {'Rock': 1, 'Paper': 2, 'Scissors': 3, 'Error': -1000}


total_sum = 0 
draw = 3 
win = 6
for i,j in t:
    print(i, j)
    sum = 0 
    s1, s2 = char_to_shape(i), char_to_shape(j)
    if s1 == s2:
        sum += draw
        sum += d[s2]

    elif s1 == 'Rock':
        if s2 == 'Paper':
            sum += win
            sum += d[s2]
        else:
            sum += d[s2]
    elif s1 == 'Paper':
        if s2 == 'Scissors':
            sum += win
            sum += d[s2]
        else:
            sum += d[s2]
    elif s1 == 'Scissors':
        if s2 == 'Rock':
            sum += win
            sum += d[s2]
        else:
            sum += d[s2]

    total_sum += sum


print(total_sum)

### Part 2 

# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win 


    

def win_condition(c):
    if c in ['X']:
        return 'Lose'
    elif c in ['Y']:
        return 'Draw'
    elif c in ['Z']:
        return 'Win'
    else:
        return 'Error'
    
def corresponding_shape(shape, win_condition):
    if win_condition == 'Win':
        if shape == 'Rock':
            return 'Paper'
        elif shape == 'Paper':
            return 'Scissors'
        elif shape == 'Scissors':
            return 'Rock'
    elif win_condition == 'Draw':
        return shape
    elif win_condition == 'Lose':
        if shape == 'Rock':
            return 'Scissors'
        elif shape == 'Paper':
            return 'Rock'
        elif shape == 'Scissors':
            return 'Paper'

corrected_sum = 0 
condition_score = {'Win': 6, 'Draw': 3, 'Lose': 0}
for i,j in t:
    print(i, j)
    sum = 0 
    s1, s2 = char_to_shape(i), win_condition(j)
    print(s1,s2)
    shape = corresponding_shape(s1, s2)
    print(shape)
    sum += condition_score[s2]
    sum += d[shape]
    corrected_sum += sum

print(corrected_sum)

