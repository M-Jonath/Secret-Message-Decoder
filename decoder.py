message_file = "coding_qual_input.txt"

def decode(message_file):
    message = []
    step = 1
    lines = sorted(open(message_file, "r").readlines(), key=lambda line: int(line.split(' ')[0]))
    for line in lines:
      number, word = line.split(' ')
      if int(number) == step:
        message.append(word.strip())
        step = step + len(message) + 1
    return ' '.join(message)

print(decode(message_file))

