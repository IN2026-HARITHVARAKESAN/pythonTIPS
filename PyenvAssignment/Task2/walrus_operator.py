"""This script demonstrates the use of the walrus operator (:=) in Python."""
if __name__ == "__main__":
    print("Enter text. Press Enter without typing to stop.")

    while (text := input("Enter text: ")) != "":
        print("You entered:", text)

    print("Program completed.")