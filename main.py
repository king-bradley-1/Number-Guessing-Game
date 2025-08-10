import random as r

levels = {
    'e': 10,
    'h': 5,
    'x': 0
}


def __start_game(actual, lives):
    won = False
    while lives > 0:
        guess = input("Guess the number: ")
        try:
            guess = int(guess)
            if guess < actual:
                print("Go Higher.")
                lives -= 1
            elif guess > actual:
                print("Go Lower.")
                lives -= 1
            else:
                print("You got it!")
                won = True
                break
        except ValueError:
            print("Invalid input. Guess again.")
            lives -= 1
    if won:
        print("Congratulations!")
    else:
        print(f"Game Over! The correct answer was: {actual}")


def guess_the_number():
    actual = r.randint(0, 100)
    message = "Welcome to the number guessing game. Choose the level:\n  Easy mode will grant 10 lives.\n  Hard mode will grant 5 lives.\nPress 'e' for easy mode, 'h' for hard mode and 'x' to exit: "
    start = input(message).lower()
    if start not in levels.keys():
        print("Invalid input.")
        guess_the_number()
    else:
        __start_game(actual, levels.get(start))


if __name__ == "__main__":
    guess_the_number()
