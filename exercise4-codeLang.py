# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

message = input("Enter your message: ")
choice = input("Do you want to code or decode the message? ")

if choice == "code" or choice == "Code":
    words = message.split()
    for word in words:
        if len(word) >= 3:
            word = word[1:] + word[0]
            word = "abc" + word + "def"
        else:
            word = word[::-1]
        print(word, end=" ")
elif choice == "decode" or choice == "Decode":
    words = message.split()
    for word in words:
        if len(word) < 3:
            word = word[::-1]
        else:
            word = word[3:-3]
            word = word[-1] + word[:-1]
        print(word, end=" ")

        