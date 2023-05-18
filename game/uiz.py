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
still_guessing = True

def start():
    print ("Let's challenge your brain!")
    while game():
        pass
    scores()

def game():
    player = check_answer()
    return play_again()

def check_answer():
    global score
    for key, value in quiz.items():
        print(value['question'])
        answer = input("Answer? ")
        if answer.lower() == value['answer'].lower():
            print("You get sense!")
            score +=1
            print("Your score is " + str(score) +" so far.")
            print(" ")
        else:
            print("That's wrong, the answer is " + value['answer'])
            print("Taiwo laughs as you realise you have just missed the answer. Haha!")
            print("You've scored " + str(score) +" so far.")
            print(" ")

def play_again():
    again = input("Would you like to play again? y/n ")
    if again in ("yes", "Yes", "y", "Y", "sure"):
        return again
    print("Thank you for taking the challenge")

def scores():
    global score
    print(" ")
    print("SCORES")
    print("You got " + str(score) + " out of 7 questions correctly") 
    print("Your percentage is " + str(int(score/7 * 100)) + "%")
    print("")
        

start()
