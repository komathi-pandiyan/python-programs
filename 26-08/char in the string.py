def count_occurrences(text, target_character):
    return text.count(target_character)
input_string = "hello world, how are you?"
target_char = 'o'
occurrences = count_occurrences(input_string, target_char)
print(f"The character '{target_char}' appears {occurrences} times in the string.")
