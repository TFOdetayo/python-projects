quiz = {
    "question1": {
        "question": "What's the capital of France?",
        "answer": "Paris"
    },
    "question2": {
        "question": "What's the capital of Germany?",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What's the capital of Italy?",
        "answer": "Rome"
    },
    "question4": {
        "question": "What's the capital of Spain?",
        "answer": "Madrid"
    },
    "question5": {
        "question": "What's the capital of Portugal?",
        "answer": "Lisbon"
    },
    "question6": {
        "question": "What's the capital of Switzerland?",
        "answer": "Bern"
    },
    "question7": {
        "question": "What's the capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input("Answer? ")

    if answer.lower() == value['answer'].lower():
        print('Correct')
        score += 1
        print("Your score is: " + str(score))
        print("")
        print("")

    else:
        print("Wrong!")
        print("The answer is " + value['answer'])
        print("Your score is: " + str(score))
        print("")
        print("")

print("You got " + str(score) + " out of 7 questions correctly")
print("Your percentage is " + str(int(score/7 * 100)) + "%")
print("")
print("")
print("Do you want to answer the questions again? If yes, enter A, otherwise, enter B to exit")
print("")

choice = input("Input your choice: ")

if choice == "a" or choice == "A":
    score = 0

    for key, value in quiz.items():
        print("")
        print(value['question'])
        answer = input("Answer? ")

        if answer.lower() == value['answer'].lower():
            print('Correct')
            score += 1
            print("Your score is: " + str(score))
            print("")
            print("")

        else:
            print("Wrong!")
            print("The answer is " + value['answer'])
            print("Your score is: " + str(score))
            print("")
            print("")
    print("You got " + str(score) + " out of 7 questions correctly")
    print("Your percentage is " + str(int(score/7 * 100)) + "%")
    print("")
else:
    quit()
