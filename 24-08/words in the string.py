def word_iterator(text):
    words = text.split()
    for word in words:
        yield word


iterator = word_iterator("This is a sentence.")

for word in iterator:
    print(word)