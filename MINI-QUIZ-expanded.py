import random
import os

bestscore = 0
player_best = "No Player"
    
quiz = [
    {
        "question": "What is the capital city of Japan?",
        "option": ["A. Seoul", "B. Tokyo", "C. Kyoto", "D. Osaka"],
        "answer": "b"
    },
    {
        "question": "What does CPU stand for?",
        "option": ["A. Central Performance Unit", "B. Central Processing Unit", "C. Computer Power Unit", "D. Control Processing Unit"],
        "answer": "b"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "option": ["A. Venus", "B. Jupiter", "C. Mars", "D. Saturn"],
        "answer": "c"
    },
    {
        "question": "Who created Python?",
        "option": ["A. Dennis Ritchie", "B. Mark Zuckerberg", "C. Guido van Rossum", "D.  Elon Musk"],
        "answer": "c"
    },
    {
        "question": "What does the term ‘bug’ originally refer to in programming?",
        "option": ["A. A virus", "B. A fly inside a hard drive", "C. A mistake in the code", "D. A hardware problem"],
        "answer": "c"
    },
    {
        "question": "Which gas do plants primarily absorb from the atmosphere?",
        "option": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "c"
    },
    {
        "question": "Which element has the chemical symbol 'Au'?",
        "option": ["A. Silver", "B. Gold", "C. Copper", "D. Argon"],
        "answer": "b"
    },
    {
        "question": "In which continent is the Amazon Rainforest located?",
        "option": ["A. Africa", "B. Asia", "C. South America", "D. Australia"],
        "answer": "c"
    },
    {
        "question": "What is the square root of 144?",
        "option": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "c"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "option": ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo"],
        "answer": "b"
    }   
]
print("="*30)

def load_bestscore():
    global bestscore
    global player_best
    if os.path.exists("bestscore.txt"):
        with open("bestscore.txt", "r", encoding="utf-8") as file:
            content = file.read().strip()
            try:
                player_bests, bestscores = content.split(":")
                bestscore = int(bestscores)
                player_best = player_bests.strip()
            except ValueError:
                bestscore = 0
                player_best = "No Player"

load_bestscore()

score_count = 0

def main_menu():
    while True:
        print(f"\nWelcome to the Mini Quiz!")
        print(f"==========================\n")
        print(f"1. Start Quiz")
        print(f"2. View Best Score")
        print(f"3. Reset Best Score")
        print(f"4. Exit")

        choice = input("\nPlease select an option (1-4): ").strip()
        if choice == "1":
            print(f"\nHere comes the questions!!\n")
            play_quiz()
            break
        elif choice == "2":
            load_bestscore()    
            print(f"\nBestscore ---> {player_best} : {bestscore}\n")
        elif choice == "3":
            reset_score()
            print(f"Your bestscore has been reset to 0!\n")
        elif choice == "4":
            print("Exiting the quiz. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")


def play_quiz():
    random.shuffle(quiz)
    for question_picked in quiz:
        print(question_picked["question"])
        for option in question_picked["option"]:
            print(option)

        user_input = check_input()
        check_answer(user_input, question_picked)

    if score_count < len(quiz):
        print(f"Nice try, You answer {score_count} out of {len(quiz)} questions right!! You can do better !!")
    elif score_count == len(quiz):
        print(f"GREAT JOB!! You do all {len(quiz)} questions right!")


def check_input():
    while True:
        answer = input(f"\nYour Answer (A, B, C, or D):  ").strip().lower()
        if answer in ["a","b","c","d"]:
            return answer
        else:
            print(f"❌ Invalid input! Please enter only A, B, C, or D.")           

def check_answer(user_input, question_picked):
    global score_count
    if user_input.lower() == question_picked["answer"]:
        print(f"Awesome, You're Right!!\n")
        score_count += 1

    else:
        print(f"Oof, Wrong Answer!\n")


def reset_score():
    with open("bestscore.txt", "w", encoding="utf-8") as file:
        file.write(f"No Player : 0")

def record_score():
    player_best = input(f"\nYou got a new bestscore of {score_count}!!\nPlease enter your name: ").strip().title()
    with open("bestscore.txt", "w", encoding="utf-8") as file:
        file.write(f"{player_best} : {score_count}")

def check_score():
    global bestscore
    global score_count
    global player_best
    if os.path.exists("bestscore.txt"):
        with open("bestscore.txt", "r", encoding="utf-8") as file:
            content = file.read().strip()
            try:
                player_bests, bestscores = content.split(":")
                bestscore = int(bestscores)
                player_best = player_bests.strip()
            except ValueError:
                bestscore = 0
                player_best = "No Player"


    if score_count > bestscore:
        record_score()
        bestscore = score_count

    
while True:
    
    score_count = 0
    main_menu()
    check_score()

    main_menu()
    break