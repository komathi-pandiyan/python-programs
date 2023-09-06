String1 = input("Enter the 1st string :")
String2 = input("Enter the 2nd string :")
if len(String1) != len(String2):
    print("Strings are not anagram")
else:
    String1 = sorted(String1)
    String2 = sorted(String2)
if String1 == String2:
    print("Strings are anagram")
else:
    print("Strings are not anagram")