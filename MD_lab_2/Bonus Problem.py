import random


def generate_secret_code():
    colors = ['R', 'G', 'B', 'Y', 'O', 'P']  # Colors: Red, Green, Blue, Yellow, Orange, Purple
    secret_code = random.sample(colors, 4)  # Generate a random code of 4 colors
    return secret_code


def evaluate_guess(secret_code, guess):
    exact_matches = 0
    color_matches = 0

    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            exact_matches += 1
        elif guess[i] in secret_code:
            color_matches += 1

    return exact_matches, color_matches


def main():
    print("Welcome to the Mastermind game!")
    print("Colors: R - Red, G - Green, B - Blue, Y - Yellow, O - Orange, P - Purple")
    print("Try to guess the secret code in as few attempts as possible.")

    secret_code = generate_secret_code()
    attempts = 0
    max_attempts = 10

    while attempts < max_attempts:
        guess = input("\nEnter your guess (4 colors, no spaces): ").upper()

        if len(guess) != 4 or not all(color in 'RGBYOP' for color in guess):
            print("Invalid input. Please enter a valid guess.")
            continue

        attempts += 1
        exact_matches, color_matches = evaluate_guess(secret_code, guess)

        print(f"Attempt {attempts}: {guess} - Exact Matches: {exact_matches}, Color Matches: {color_matches}")

        if exact_matches == 4:
            print("Congratulations! You've guessed the secret code!")
            break

    if attempts == max_attempts and exact_matches != 4:
        print(f"\nSorry, you've run out of attempts. The secret code was {secret_code}.")
if __name__ == "__main__":
    main()