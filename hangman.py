import random
import string
print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
word = list(random.choice(words))
i = list(len(word) * "-")
lives = 8
r = set()


def menu():
    u = input('Type "play" to play the game, "exit" to quit:')
    return game() if u == "play" else 0


def game():
    global lives
    while lives > 0:
        print()
        print("".join(i))
        user = input("Input a letter: ")
        if len(user) > 1:
            print("You should input a single letter")
        elif user not in string.ascii_lowercase:
            print("Please enter a lowercase English letter")
        elif user in r:
            print("You've already guessed this letter")
        elif user in word:
            for j in range(len(word)):
                if word[j] == user:
                    i[j] = user
                    r.add(user)
                    if not i.count("-"):
                        print("""You guessed the word java!
                                 You survived!""")
                        return menu()
        elif user not in word:
            print("That letter doesn't appear in the word")
            r.add(user)
            lives -= 1
            if lives == 0:
                print("You lost!")
                return menu()


menu()
