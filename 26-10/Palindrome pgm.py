def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
if __name__ == "__main__":
    input_string = "A man a plan a canal Panama"
    result = is_palindrome(input_string)
    if result:
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")