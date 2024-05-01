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

'''
To start, my function creates an empty list called message - this will store the decrypted message. 
Then I have created a counter steps. This will allow my function to check the numbered lines against 
the current 'step' to identify which word comes next in the message. After that I open the message 
file and read each line onto a seperate list item stored in lines. During the readlines() method, I
am sorting the lines with the sorted() method. Each line gets placed into ascending order based on 
the number extracted from the first part of each string with int(line.split(' ')[0]. In this part,
the line.split(' ')[0] is splitting each line into separate list items based on a space (' ') and
returning the first item - index 0 - which is the number. The result of the split is then turned
into an integer to finally be used to sort the lines. Now that the lines are in numerical order, the
lines are again split with .split(' ') - this time the first item is named number and the second is
named as word. once these are split we use an if statement to check if the lines number is equal to
the step we are up to. The first step is always 1. Once the line with number == 1 is found the word
part of that line is added to the end of the message list and while doing so has any excess spaces
striped with .strip(). once the word is added to message, the step value is updated to reflect the
next triangular number. This is done by taking the current step value, adding the new length of the
message list, and then adding 1. i.e. after adding the first word, the step was 1, and the message
length is also one, so 1 + 1 + 1 = 3, after the second word is added, step = 3 and Len(message) = 2
so the next step will be 3+2+1 = 6. This continues until the end of the document. After the whole
document is read and decoded, the function returns each item in the message, joined with a space (' ').
'''