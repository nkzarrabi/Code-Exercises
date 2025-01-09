from itertools import product

# Part 1: Evolve secret numbers
def evolve_secret(secret):
    # Step 1: Multiply by 64, mix, and prune
    secret = (secret ^ (secret * 64)) % 16777216
    # Step 2: Divide by 32 (integer division), mix, and prune
    secret = (secret ^ (secret // 32)) % 16777216
    # Step 3: Multiply by 2048, mix, and prune
    secret = (secret ^ (secret * 2048)) % 16777216
    return secret

# Part 2: Simulate buyers and prices
def simulate_prices(initial_secret, iterations=2000):
    prices = []
    secret = initial_secret
    for _ in range(iterations):
        secret = evolve_secret(secret)
        prices.append(secret % 10)  # Extract the last digit as the price
    return prices

# Find the first occurrence of a change sequence in a price list
def find_sequence(prices, sequence):
    changes = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
    seq_len = len(sequence)
    for i in range(len(changes) - seq_len + 1):
        if changes[i:i + seq_len] == sequence:
            return prices[i + seq_len]  # Price after the sequence occurs
    return 0  # Sequence not found

# Main function
def maximize_bananas(initial_secrets):
    max_bananas = 0
    best_sequence = None
    # Generate all possible sequences of four price changes
    all_sequences = list(product(range(-9, 10), repeat=4))  # Changes from -9 to 9
    for sequence in all_sequences:
        total_bananas = 0
        for secret in initial_secrets:
            prices = simulate_prices(secret)
            bananas = find_sequence(prices, sequence)
            total_bananas += bananas
        if total_bananas > max_bananas:
            max_bananas = total_bananas
            best_sequence = sequence
    return max_bananas, best_sequence

# Example input
flag = False
file = 'example.txt' if flag else 'input.txt'
initial_secrets = open(file, 'r').read().splitlines()
initial_secrets = [int(secret) for secret in initial_secrets]

# Solve for maximum bananas
max_bananas, best_sequence = maximize_bananas(initial_secrets)
print("Maximum bananas:", max_bananas)
print("Best sequence:", best_sequence)