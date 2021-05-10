def main():
    inputText = input("Please enter a string of plaintext:").lower()
    inputValue = int(input("Please enter the value of the key:")) # use int(), don't eval unless you read more about it
    inputEorD = input("Please enter e (to encrypt) or d (to decrypt) ")
    codedMessage = ""

    if inputEorD == "e":
        for ch in inputText:
            codedMessage += chr((ord(ch) - 97 + inputValue)%26 + 97)
    elif inputEorD =="d":
        for ch in inputText:
            codedMessage += chr((ord(ch) - 97 - inputValue)%26 + 97)
    else:
        print("You did not enter E/D! Try again!!")
    print("The text inputed:", inputText,  ".Is:", inputEorD, ".By the key of",inputValue, ".To make the message", codedMessage)

main()