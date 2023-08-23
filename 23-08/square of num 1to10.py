def square_iterator():
    for i in range(1, 11):
        yield i * i


iterator = square_iterator()

for i in iterator:
    print(i)