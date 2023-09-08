def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("----------------------------------")
        print(key)
        for option in options[question_num - 1]:
            print(option)
        guess = input("Enter (A, B, C or D): ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0


def display_score(correct_guesses, guesses):
    print("Results")
    print("Answers: ", end="")
    for question in questions:
        print(questions.get(question), end="")
    print()

    print("Guesses: ", end="")
    for guess in guesses:
        print(guess, end="")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is: " + str(score) + "%")


def play_again():
    response = input("Do you want to play again (y/n): ")
    response = response.upper()

    if response == "Y":
        return True
    else:
        return False


questions = {
    "Who created Python: ": "A",
    "What year was Python created: ": "B",
    "Python is a tribute to which comedy group: ": "C",
    "Is the Earth round: ": "A"
}

options = [
    ["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. None of the options"]
]

new_game()

while play_again():
    new_game()

print("Bye")
