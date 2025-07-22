import random
from quiz_data import quiz 
from score import check_score, record_score
import shared

def play_quiz():
    random.shuffle(quiz)
    for q in quiz:
        print(q["question"])
        for opt in q["option"]:
            print(opt)

        user_input = check_input()
        check_answer(user_input, q)

    check_score()


    if shared.score_count < len(quiz):
        print(f"Nice try, You answer {shared.score_count} out of {len(quiz)} questions right!! You can do better !!")
    elif shared.score_count == len(quiz):
        print(f"GREAT JOB!! You do all {len(quiz)} questions right!")


def check_input():
    while True:
        answer = input(f"\nYour Answer (A, B, C, or D):  ").strip().lower()
        if answer in ["a","b","c","d"]:
            return answer
        else:
            print(f"❌ Invalid input! Please enter only A, B, C, or D.")           

def check_answer(user_input, q):
    if user_input.lower() == q["answer"]:
        print(f"Awesome, You're Right!!\n")
        shared.score_count += 1

    else:
        print(f"Oof, Wrong Answer!\n")