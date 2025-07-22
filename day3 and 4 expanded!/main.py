import random
from quiz_data import quiz
from logic import play_quiz, check_input, check_answer
from score import load_bestscore, record_score, check_score, reset_score
import shared

load_bestscore()
player_bests = "No Player"
bestscores = 0

def main():
    global player_bests, bestscores
    player_bests, bestscores = load_bestscore()
    print("="*50)


    while True:
        print(f"\n\nMAIN MENU\n")
        player_bests, bestscores = load_bestscore()
        print(f"Welcome to the Quiz Game!\nBest Score: {player_bests} : {bestscores}\n")
        print(f"1. Start Quiz")
        print(f"2. View Best Score")
        print(f"3. Reset Best Score")
        print(f"4. Exit")
        print(f"\nLast Score: {shared.last_score}\n")

        choice = input("\nPlease select an option (1-4): ").strip()
        if choice == "1":
            print(f"\nHere comes the questions!!\n")
            play_quiz()
            continue
        elif choice == "2":
            player_bests, bestscores = load_bestscore()
            print(f"\nBestscore ---> {player_bests} : {bestscores}\n")
        elif choice == "3":
            reset_score()
            print(f"Your bestscore has been reset to 0!\n")
        elif choice == "4":
            print("Exiting the quiz. Goodbye!")
            exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()