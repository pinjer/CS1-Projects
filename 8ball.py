import random

while True:
    question = input("Ask a question.\nQuestion: ")

    answers = random.randint(1, 8)

    if question == "":
        break
    elif answers == 1:
        print("As I see it, yes.\n")
    elif answers == 2:
        print("Reply hazy, try again.\n")
    elif answers == 3:
        print("Don't count on it.\n")
    elif answers == 4:
        print("It is certain.\n")
    elif answers == 5:
        print("Most likely.\n")
    elif answers == 6:
        print("Yes.\n")
    elif answers == 7:
        print("My reply is no.\n")
    elif answers == 8:
        print("My sources say no.\n")
    else:
        print("Not a valid input, run program again.")
        break