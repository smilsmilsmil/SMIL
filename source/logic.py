import random
import score
import shared
import os
import json
import string

def play_quiz():
    shared.score_count = 0

    while True:
        questions = []  # Always initialize questions as an empty list
        if os.path.exists("quiz_data_nested.json"):
            with open("quiz_data_nested.json", "r") as file:
                try:
                    data = json.load(file)
                except json.JSONDecodeError:
                    data = {"questions": [], "bestscores": {}}

        print(f"\n\nThese are the categories!")
        categories = [q['category'] for q in data.get("questions", [])]
        unique_categories = list(dict.fromkeys(categories))  # Remove duplicates, keep order
        for idx, cat in enumerate(unique_categories, 1):
            print(f"{idx}. {cat}")
    
        print(f"\n")
        print(f"====(Input 0 to abort)====")

        while True:
            
            try:
                cat_input = int(input(f"Which category of the quiz you would like to take?"))
                if cat_input in range(1, len(unique_categories) + 1):
                    selected_category = unique_categories[cat_input - 1]
                    break
            
                if cat_input == 0:
                    print("Exiting to the main menu.")
                    return
            
                else:
                    print(f"❌ Invalid input! Please select a valid category number.")
                    continue
            except ValueError:
                print(f"❌ Invalid input! Please enter a number between 1 and {len(unique_categories)} or 0 to exit.")
                continue

        while True:
            questions_in_category = [q for q in data.get("questions", []) if q['category'] == selected_category]
            print(f"The Category {selected_category} has {len(questions_in_category)} total questions.")
            difficulty = input(f"How many would you take?\n Easy ---> <5 questions\n Medium = ----> 5-10 questions\n Hard ---> >10 questions\nPlease select a difficulty level: ").strip().lower()
            if difficulty in ["easy", "medium", "hard"]:
                print("You selected:", difficulty)
                break
            else:
                print(f"❌ Invalid input! Please select a valid difficulty level (easy, medium, hard).")
                continue

        
        while True:
            questions_selected = [q for q in data.get("questions", []) if q['category'] == selected_category]
            random.shuffle(questions_selected)
            # Determine number of questions based on difficulty
            if difficulty == "easy":
                num_questions = min(5, len(questions_selected))
            elif difficulty == "medium":
                num_questions = min(10, len(questions_selected))
            else:  # hard
                num_questions = len(questions_selected)
            questions_to_ask = questions_selected[:num_questions]
            for idx, q in enumerate(questions_to_ask, 1):
                print(q['question'])
                for letter, option in zip(string.ascii_lowercase, q['option']):
                    print(f"{letter}. {option}")

                user_input = check_input()
                check_answer(user_input, q)
            
            print(f"\nYour score is {shared.score_count} out of {len(questions_to_ask)}!\n")
            break

        score.check_score(selected_category, difficulty, shared.score_count)

        break
                

                

        


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