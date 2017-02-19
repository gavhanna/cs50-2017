import sys

if len(sys.argv) != 1:
    print("Please enter a single integer argument.")

key = int(sys.argv[1])
sentence = input("Enter a sentence: ")


new_word = ""
for c in sentence:
    if c.isalpha():
        
        if c.isupper():
            char_num = ord(c) + key
            if char_num < 91:
                new_word += chr(char_num)
            else:
                new_word += chr(char_num - 26)
        
        if c.islower():
            char_num = ord(c) + key
            if char_num < 163:
                new_word += chr(char_num)
            else:
                new_word += chr(char_num - 26)
    else:
        new_word += c
        
print(new_word)