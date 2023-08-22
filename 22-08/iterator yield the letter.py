def alphabet_iterator():
    for letter in "abcdefghijklmnopqrstuvwxyz":
        yield letter


iterator = alphabet_iterator()

for letter in iterator:
    print(letter)