import quiz_data
from logic import play_quiz, check_input, check_answer
from score import bestscore_menu, view_bestscore, reset_score


def main(): # As the Main Menu
    print("="*50)


    while True:
        print(f"\n\nMAIN MENU\n")
        print(f"Welcome to the Quiz Game!")
        print(f"1. Start Quiz")
        print(f"2. View Best Score")
        print(f"3. Reset Best Score")
        print(f"4. Edit Questions")
        print(f"5. Exit")

        choice = input("\nPlease select an option : ").strip()
        if choice == "1":
            play_quiz()
            continue
        elif choice == "2":
            bestscore_menu()
            continue
        elif choice == "3":
            reset_score()
            print(f"Your bestscore has been reset to 0!\n")
        elif choice == "4":
            while True:
                print(f"\n\nEdit Questions Menu")
                print(f"1. Add Question")
                print(f"2. Delete Question")
                print(f"3. View Questions")
                print(f"4. Back to Main Menu")

                edit_choice = input("Select an option: ").strip()
                if edit_choice == "1":
                    quiz_data.add_question()
                elif edit_choice == "2":
                    quiz_data.delete_question()
                elif edit_choice == "3":
                    quiz_data.view_questions()
                elif edit_choice == "4":
                    break
                else:
                    print("Invalid choice. Please try again.")
                    
        elif choice == "5":
            print("Exiting the quiz. Goodbye!")
            exit()
        else:
            print("Invalid input. Try numbers from 1-5!.")

if __name__ == "__main__":
    main()