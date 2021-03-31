import sys


no_of_tries = 5
word = input("Secret Password: ")
used_letters = []


def find_indexes(word, letter):
    indexes = []
    for index, letter_in_word in enumerate(word):
        if letter == letter_in_word:
            indexes.append((index))
    return indexes


def show_state_of_game():
    print()
    print("".join(user_word))
    print("Number of tries: ", no_of_tries)
    print("Used letters: ", used_letters)
    print()


user_word = []
for _ in word:
    user_word.append("_")


while True:
    letter = input("Choose letter: ")
    if letter not in used_letters:
        used_letters.append(letter)
    else:
        print("Letter already used!")
        pass
    found_indexes = find_indexes(word, letter)

    if len(found_indexes) == 0:
        print("Letter not found")
        no_of_tries -= 1

        if no_of_tries == 0:
            print("Game over")
            sys.exit(0)
    else:
        for index in found_indexes:
            user_word[index] = letter

        if "".join(user_word) == word:
            print("Congratulation, This is a word. You Win")
            sys.exit(0)
    show_state_of_game()
