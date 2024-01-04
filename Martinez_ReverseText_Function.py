while True:
    text = input("\nEnter a string: ")
    if text.isalpha():  # to determine if it is composed only to letters
        reverseText = text[::-1]  # to make the string reverse
        print("Output:", reverseText)
        break
    else:
        print("Error Reported! Enter text only.")
