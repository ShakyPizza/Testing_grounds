import random


def play_round():
    random_number = random.randint(1, 2)
    guessed_correctly = False
    attempts = 0
    max_score = 10

    while not guessed_correctly and attempts < 10:
        attempts += 1
        print("What is you guess? ")
        guess = int(input())

        if guess < random_number:
            print("Your guess is too low")

        elif guess > random_number:
            print("Your guess is too high")

        else:
            print("Congratulations! you've guessed the correct number!")
            guessed_correctly = True

    score = max(max_score - attempts + 1, 0)

    return score

total_score = 0 

while True:
    total_score += play_round()

    play_again = input("Do you want to play again? (yes/no)").strip().lower()
    if play_again not in ["yes", "y", "ye"]:
        print(f"Your total score after this round is: {total_score}")
        break

print(f"Your total score after all rounds is: {total_score}")