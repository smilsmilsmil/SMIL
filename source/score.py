import os
import shared
import json

def ensure_bestscores_categories(): # Update Bestscore on a New Category
    with open("quiz_data_nested.json", "r",encoding="utf-8") as file:
        data = json.load(file)
        bestscores = data.get("bestscores", {})
        questions = data.get("questions", [])
        categories = set(q["category"] for q in questions)
        updated = False

        for cat in categories:
            if cat not in bestscores:
                bestscores[cat] = {
                    "easy": 0, 
                    "easyname": "none",
                    "medium": 0, 
                    "mediumname": "none",
                    "hard": 0, 
                    "hardname": "none"
                }
                updated = True

        if updated:
            data["bestscores"] = bestscores
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()

def bestscore_menu(): # Score Menu
    while True:
        print("\nBest Score Menu")
        print("1. View Best Score")
        print("2. Reset Best Score")
        print("0. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            view_bestscore()
        elif choice == "2":
            reset_score()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def view_bestscore():
    if not os.path.exists("quiz_data_nested.json"):
        print("Best score file not found.")
    else:
        with open("quiz_data_nested.json","r", encoding="utf-8") as file:
            data = json.load(file)
           
    
    while True:
        with open("quiz_data_nested.json", "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                print("Error reading the quiz data file. Please check the file format.")
                return
        questions = data.get('questions', [])
        if not questions:
            print("No categories found.")
            break
        unique_categories = list(dict.fromkeys(q['category'] for q in questions))
        for idx, cat in enumerate(unique_categories, 1):
            print(f"{idx}. {cat}")

        print(f"\n====(Input 0 to abort)====")
        try:
            best_category = int(input(f"\n\nWhich category do you want to see the best score for? : "))
            if best_category == 0:
                print("Exiting to the main menu.")
                break
            elif 1 <= best_category <= len(unique_categories):
                category_to_view = unique_categories[best_category - 1]
                bestscores = data.get("bestscores", {})
                if category_to_view in bestscores:
                    bestscore = bestscores[category_to_view]
                    print(f"Best scores for category '{category_to_view}':")
                    print(f"Easy: {bestscore['easy']} by {bestscore['easyname']}")
                    print(f"Medium: {bestscore['medium']} by {bestscore['mediumname']}")
                    print(f"Hard: {bestscore['hard']} by {bestscore['hardname']}")
                    menu_input = input("Press Enter to return to the main menu.")
                    if menu_input == "":
                        print("Returning to the main menu.")
                        break
                else:
                    print(f"No best scores found for category '{category_to_view}'.")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

def check_score(selected_category, difficulty, score_count):
    if not os.path.exists("quiz_data_nested.json"):
        print("No quiz data found.")
        return
    
    with open("quiz_data_nested.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    bestscores = data.get("bestscores", {})


    if selected_category not in bestscores:
        bestscores[selected_category] = {
            "easy": 0, 
            "easyname": "none",
            "medium": 0, 
            "mediumname": "none",
            "hard": 0, 
            "hardname": "none"
        }

    best_for_difficulty = bestscores[selected_category][difficulty]
    if score_count > best_for_difficulty:
        print(f"New best score for ({difficulty}) {selected_category}: {score_count}!!")
        player_best = input(f"Please enter your name: ").strip().title()
        bestscores[selected_category][difficulty] = score_count
        bestscores[selected_category][f"{difficulty}name"] = player_best
        with open("quiz_data_nested.json", "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4) # Part where the data being dumped into the json
        print(f"New best score recorded for {selected_category} ({difficulty}): {score_count} by {player_best}")
    else:
        print(f"Your score = {score_count}, best score in the same category is {best_for_difficulty} by {bestscores[selected_category][f'{difficulty}name']}.")




def reset_score():
    with open("quiz_data_nested.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
        print(f"\n\nThese are the categories!")
        categories = [q['category'] for q in data.get("questions", [])]
        unique_categories = list(dict.fromkeys(categories))  # Remove duplicates, keep order
        for idx, cat in enumerate(unique_categories, 1):
            print(f"{idx}. {cat}")
    
        print(f"\n")
        print(f"====(Input 0 to abort)====\n")
        try:
            select_category = input("Enter the category you want to reset the best score for: \n\n WARNING THIS WILL DELETE ALL \nDIFFICULTY ON THE CATEGORY ").strip()
            if select_category in data.get("bestscores", {}):
                confirm = input(f"Are you sure you want to reset the best scores for category '{select_category}'? (yes/no): ").strip().lower()
                if confirm == "yes":
                    data["bestscores"][select_category] = {
                        "easy": 0,
                        "easyname": "none",
                        "medium": 0,
                        "mediumname": "none",
                        "hard": 0,
                        "hardname": "none"
                    }
                    file.seek(0)
                    json.dump(data, file, indent=4)
                    file.truncate()
                    print(f"Best scores for category '{select_category}' have been reset.")
                else:
                    print("Reset operation cancelled.")
            else:
                print(f"Category '{select_category}' not found.")
        except ValueError:
            print(f"Invalid input. Please enter a valid category name.")