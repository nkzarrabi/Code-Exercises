def decode(message_file):
    num_dict = {}
    with open(message_file, 'r') as file:
        for line in file:
            num, word = line.strip().split()
            num_dict[int(num)] = word 

    curr_line = 1
    message_words = []

    while True:
        last_word_idx = (curr_line * (curr_line + 1)) // 2
        if last_word_idx in num_dict:
            message_words.append(num_dict[last_word_idx])
            curr_line += 1
        else:
            break

    return ' '.join(message_words)




message_file = 'message.txt'

# Decoding the message
decoded_message = decode(message_file)
print(decoded_message)