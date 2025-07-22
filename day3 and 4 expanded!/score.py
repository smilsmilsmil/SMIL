import os
import shared

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
                return ("No Player", 0)
            return (player_best, bestscore)
    else:
        return ("No Player", 0)

def record_score():
    player_best = input(f"\nYou got a new bestscore of {shared.score_count}!!\nPlease enter your name: ").strip().title()
    with open("bestscore.txt", "w", encoding="utf-8") as file:
        file.write(f"{player_best} : {shared.score_count}")

def check_score():
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


    if shared.score_count > bestscore:
        record_score()
        bestscore = shared.score_count

    shared.last_score = shared.score_count
    shared.score_count = 0
    
def reset_score():
    with open("bestscore.txt", "w", encoding="utf-8") as file:
        file.write(f"No Player : 0")