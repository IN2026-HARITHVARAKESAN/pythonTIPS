"""This is a game implemented using a generator function. The player can navigate through different locations and make choices that affect the outcome of the game."""

def adventure_game():
    """A simple text-based adventure game implemented as a generator function."""

    location = "forest"

    try:
        while True:

            if location == "forest":
                message = "You are in a forest. Go North or South?"
                valid_choices = ["north", "south"]

            elif location == "cave":
                message = "You found a cave! Enter or go back?"
                valid_choices = ["enter", "back"]

            elif location == "treasure":
                message = "You found a treasure chest! Open or leave?"
                valid_choices = ["open", "leave"]

            elif location == "river":
                message = "You reached a river! Swim or go back?"
                valid_choices = ["swim", "back"]

            try:
                choice = yield message

            except ValueError as error:
                choice = yield f"Invalid choice: {error}. Try again: {message}"

            choice = choice.lower().strip()

            if choice == "quit":
                yield "Goodbye! Thanks for playing!"
                return

            if location == "forest":
                if choice == "north":
                    location = "cave"
                elif choice == "south":
                    location = "river"

            elif location == "cave":
                if choice == "enter":
                    location = "treasure"
                elif choice == "back":
                    location = "forest"

            elif location == "treasure":
                if choice == "open":
                    yield "Congratulations! You found the treasure. YOU WIN!"
                    return
                elif choice == "leave":
                    location = "cave"

            elif location == "river":
                if choice == "swim":
                    yield "The current swept you away. GAME OVER!"
                    return
                elif choice == "back":
                    location = "forest"

    finally:
        print("Game generator closed.")


def play_game():
    """Runs the adventure game in the terminal."""

    game = adventure_game()

    message = next(game)

    while True:

        print("\n" + message)

        choice = input("Your choice (or quit): ").strip().lower()

        if choice == "quit":
            message = game.send("quit")
            print("\n" + message)
            game.close()
            break

        valid_choices = {
            "forest": ["north", "south"],
            "cave": ["enter", "back"],
            "treasure": ["open", "leave"],
            "river": ["swim", "back"]
        }
        if choice not in valid_choices[get_current_location(game)]:
            message = game.throw(ValueError(choice))
        else:
            try:
                message = game.send(choice)
            except StopIteration:
                print("\nGame finished!")
                break


def get_current_location(game):
    """Return the current location stored in the game."""
    return game.gi_frame.f_locals["location"]


if __name__ == "__main__":
    play_game()