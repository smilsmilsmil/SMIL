import json
import os  

def add_question():
    while True:
        questions = []  # Always initialize questions as an empty list
        if os.path.exists("questions.json"):
            with open("questions.json", "r") as file:
                try:
                    questions = json.load(file)
                except json.JSONDecodeError:
                    questions = []

        while True:
            question = input("Enter the question: ").strip()
            if not question:
                print("Question cannot be empty. Please try again.")
                continue
            if question:
                break

        while True:
            option = []
            for i in range(4):
                while True:
                    opt = input(f"Enter the questions option! ({i+1}): ").strip()
                    if not opt:
                        print("Option cannot be empty. Please try again.")
                        continue
                    option.append(opt)
                    break
            break

        while True:
            answer = input("Enter the correct answer (A, B, C, or D): ").strip().lower()
            if answer in ["a", "b", "c", "d"]:
                break
            else:
                print("Invalid answer choice. Please enter A, B, C, or D.")
                continue

        while True:
            category = input("Enter the category of the question: ").strip().capitalize()
            if not category:
                print("Category cannot be empty. Please try again.")
                continue
            if category:
                break

        questions.append({
            "question": question,
            "option": option,
            "answer": answer,
            "category": category
        })

        with open("questions.json", "w") as file:
            json.dump(questions, file, indent=4)
        break

def delete_question():
    if not os.path.exists("questions.json"):
        print(f"\nNo questions found to delete.\n")
        return
    elif questions := json.load(open("questions.json")) == []:
        print(f"\nNo questions found to delete.\n")
        return
    else:
        with open("questions.json", "r") as file:
            questions = json.load(file)
            print(f"\nWhich questions category do you want to delete?")

    categories = [q['category'] for q in questions]
    unique_categories = list(dict.fromkeys(categories))  # Remove duplicates, keep order
    for idx, cat in enumerate(unique_categories, 1):
        print(f"{idx}. {cat}")
    
    print(f"\n")

    print(f"====(Input 0 to abort)====")

    while True:
        try:
            del_choice = int(input(f"Input the Number of the category you want to delete! :    "))
            if del_choice== 0:
                print("="*20)
                print("\nAborting deletion.")
                print("\n","="*20)
              
                return
            
            if 1 <= del_choice <= len(unique_categories):
                category_to_delete = unique_categories[del_choice - 1]
                break

            else:
                if len(unique_categories) == 1:
                    print(f"invalid choice. Please enter 1 or 0 to abort")
                    continue
                if len(unique_categories) > 1:
                    print(f"Invalid choice. Please enter a number between 1 and {len(unique_categories)}, or 0 to abort.")
                    continue
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"These are the questions in the category {category_to_delete} : ")
    questions_in_category = [q for q in questions if q['category'] == category_to_delete]
    for idx, q in enumerate(questions_in_category, 1):
        print(f"{idx}. {q['question']}")   

    print(f"\n====(Input 0 to abort)====")
   
    while True:
        try:  
            questions_to_del = int(input(f"\nWhich question do you want to delete from the category {category_to_delete}? : "))
            if questions_to_del == 0:
                print("="*20)
                print("\nAborting deletion.")
                print("\n","="*20)
                return 0

            if 1 <= questions_to_del <= len(questions_in_category):
                question_to_del = questions_in_category[questions_to_del - 1]
                questions.remove(question_to_del)
                with open("questions.json", "w") as file:
                    json.dump(questions, file, indent=4)
                print("="*20)
                print(f"\nQuestion deleted successfully!")
                print("\n","="*20)
                break
            else:
                if len(questions_in_category) == 1:
                    print(f"Invalid choice. Please enter 1 or 0 to abort.")
                    continue
                if len(questions_in_category) > 1:
                    print(f"Invalid choice. Please enter a number between 1 and {len(questions_in_category)}, or 0 to abort.")
                    continue
        except ValueError:
            print("Invalid input. Please enter a number.")
