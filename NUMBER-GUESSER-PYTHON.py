import random

number = random.randint(1,100)


while True:
    max_attemptsinput = (input("Pilih Easy, Medium, atau Hard? :   ")).lower()
    if max_attemptsinput == "easy":
        max_attempts = 20
        break
    if max_attemptsinput == "medium":
        max_attempts = 15
        break
    if max_attemptsinput == "hard":
        max_attempts = 10
        break
    else:
        ValueError
        print("⚠️ Masukkan jawaban yang valid ya!")
        continue

print(f"Kesempatan kamu ada {max_attempts} kali!")

attempts = 0

while True:
        
    try:
        guess = int(input("Tebak angka! (1-100) : "))
    except ValueError:  
        print("⚠️ Masukkan angka yang valid ya!")
        continue

    if guess == number:
        print(f"Selamat!! Angka tersebut adalah {number}, Kamu berhasil dalam {attempts} kali percobaan")
        exit()
    else:
        attempts += 1

    if attempts == max_attempts: 
        print(f"Yahhh.. kesempatan kamu habis! coba lagi ya!!")
        exit()

    guess_left = max_attempts - attempts

    if guess < number:
        print(f"Terlalu rendah!, kesempatan tersisa {guess_left}")
        continue
    elif guess > number:
        print(f"Terlalu tinggi!, kesempatan tersisa {guess_left}")
        continue