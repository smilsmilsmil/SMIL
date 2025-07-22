import random
import os

bestscore = 0
    
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
    }
]
print(f"\nWelcome to SMIL-quiz!!")
print(f"=======================\n")

def load_bestscore():
    global bestscore
    if os.path.exists("bestscore.txt"):
        with open("bestscore.txt", "r", encoding="utf-8") as file:
            content = file.read().strip()
            bestscore = int(content) if content else 0

load_bestscore()
print(f"Your bestscore ---> {bestscore}")


score_count = 0

def play_quiz():
    random.shuffle(quiz)
    for question_picked in quiz:
        print(question_picked["question"])
        for option in question_picked["option"]:
            print(option)

        user_input = check_input()
        check_answer(user_input, question_picked)

    if score_count < 5:
        print(f"Nice try, You answer {score_count} out of 5 questions right!! You can do better !!")
    elif score_count == 5:
        print(f"GREAT JOB!! You do all 5 questions right!")


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

def record_score():
    with open("bestscore.txt", "w", encoding="utf-8") as file:
        file.write(str(score_count))

def check_score():
    global bestscore
    global score_count
    if os.path.exists("bestscore.txt"):
        with open("bestscore.txt", "r", encoding="utf-8") as file:
            content = file.read().strip()
            bestscore = int(content) if content else 0
    else:
        bestscore= 0
    
    if score_count > bestscore:
        record_score()
        bestscore = score_count

    
while True:

    user_ready = input(f"Are you ready? Type Yes or No! :   ").strip()
    if user_ready.lower() == "yes":
        print(f"\nHere comes the questions!!")
        print(f"============================\n\n")
        score_count = 0

        play_quiz()
        check_score()
        break
        
    elif user_ready.lower() == "no":
        print(f"Alright Program Exitted\n")
        exit()
    else:
        print("Invalid Input!!\n")
        continue


while True:
    user_replay = input(f"\n\nDo you want to try again?  Type Yes or No!  :   ").strip().lower()
    if user_replay == "yes":
        load_bestscore()
        score_count = 0
        print(f"Your bestscore ---> {bestscore}")

        print(f"\nHere comes the questions!!")
        print(f"============================\n\n")

        play_quiz()
        check_score()
    elif user_replay == "no":
        print(f"\nAlright Program Exitted\n")
        exit()