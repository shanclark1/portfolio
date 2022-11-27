print("""Welcome to quiz game""")
print("""You only have 3 attempts Good luck""")
print(""":'Type Start':""")
S = input("type: ")
if S == "start" or S == "Start":
    print("let's begin")
attempts = 3
ask = 'yes'
while(ask == 'yes' and attempts > 0):
    score = 0

    print('Answer the questions')
    print("how many days in a year?")
    print("a. 365 b.360 c.370 d.375")
    answer1 = (input("Enter Answer: "))
    if (answer1 == "a") or (answer1 == "A"):
        score += 1

    print("how many days in a week?")
    print("a. 9 b.5 c.7 d.8")
    answer2 = (input("Enter Answer: "))
    if (answer2 == "c") or (answer2 == "C"):
        score += 1

    print("how many color og the rainbow?")
    print("a. 5 b.7 c.8 d.10")
    answer3 = (input("Enter Answer: "))
    if (answer3 == "b") or (answer3 == "B"):
        score += 1

    print("Multiply 3 and 22")
    print("a. 66 b. 75 c. 72 d. 60")
    answer4 = (input("Enter Answer: "))
    if (answer4 == "a") or (answer4 == "A"):
        score += 1

    print("How many bones are in the human body?")
    print ("a. 207 b. 206 c. 306 d.307")
    answer5 = (input("Enter Answer: "))
    if (answer5 == "b") or (answer5 == "B"):
        score += 1

    print("Total_score:", score)
    if (score == 5):
        print("Good job Perfect Score")
        exit()
    if (score <= 4):
        print("You've pass the test")

    if (score <= 2):
        print("Your score is low")

    if (score == 0):
        print("You failed")

    attempts -= 1

    if (attempts > 0):
        print('Attempt remaining:', attempts)
    else:
        print('End of the quiz. No more attempts left')
        break

    ask = input("do you want to try again? (yes or no):")
    if (ask == 'no'):
        print('Thanks for taking the quiz.')
        break