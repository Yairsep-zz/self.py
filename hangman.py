picture1 = ("""
    x-------x""")

picture2 = ("""
    x-------x
    |
    |
    |
    |
    |""")

picture3 = ("""
    x-------x
    |       |
    |       0
    |
    |
    |""")

picture4 = ("""
    x-------x
    |       |
    |       0
    |       |
    |
    |""")

picture5 = ("""    x-------x
    |       |
    |       0
    |      /|\ 
    |
    |""")

picture6 = ("""    x-------x
    |       |
    |       0
    |      /|\ 
    |      /
    |""")

picture7 = ("""    x-------x
    |       |
    |       0
    |      /|\ 
    |      / \ 
    |""")

HANGMAN_PHOTOS = {1: picture1, 2: picture2, 3: picture3, 4: picture4, 5: picture5, 6: picture6, 7: picture7}

HANGMAN_ASCII_ART = ("  _    _                                         \n"
                     " | |  | |                                        \n"
                     " | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  \n"
                     " |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ \n"
                     " | |  | | (_| | | | | (_| | | | | | | (_| | | | |\n"
                     " |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|\n"
                     "                      __/ |                      \n"
                     "                     |___/")


def choose_word(file_path, index):
    input_file = open(file_path, "r")
    word_Split = input_file.read().split(" ")
    numOfWords = len(word_Split)

    if index > numOfWords:
        index = index % numOfWords
    word_list = []
    for word in word_Split:
        if not word_list.__contains__(word):
            word_list.append(word)

    input_file.close()
    return word_Split[index - 1]


def is_valid_input(letter_guessed):
    if not letter_guessed.isalpha() and letter_guessed.__len__() > 1:
        return False
    elif not letter_guessed.isalpha():
        return False
    elif letter_guessed.__len__() > 1:
        return False
    else:
        return True


def check_valid_input(letter_guessed, old_letters_guessed):
    if not is_valid_input(letter_guessed):
        return False
    if letter_guessed in old_letters_guessed:
        return False
    else:
        return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if check_valid_input(letter_guessed , old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        output = ""
        for letter in old_letters_guessed:
            if not letter == old_letters_guessed[old_letters_guessed.__len__()-1]:
                output = output + letter + " -> "
            else:
                output = output + letter
        print(output)
        return False


def show_hidden_word(secret_word, old_letters_guessed):
    output = ""
    for letter in secret_word:
        if letter in old_letters_guessed:
            output = output + letter + " "
        else:
            output = output + ' _'
    print (output)


def check_win(secret_word, old_letters_guessed):
    counter = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            counter = counter +1
    if counter == secret_word.__len__():
        return True
    else:
        return False


def check_letter(secret_word, letter):
    if letter in secret_word:
        return True
    else:
        return False


def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])


def main():
    MAX_TRIES = 6
    old_letters_guessed = list()
    print(HANGMAN_ASCII_ART + "\n" + str(MAX_TRIES))
    path = input("Enter file path:")
    word_index = input("Enter index:")
    secret_word = choose_word(path, int(word_index))
    underscores = "_ " * secret_word.__len__()
    print('Let’s start!')
    print_hangman(1)
    print(underscores)
    num_of_badTries = 0
    num_of_goodTries = 0
    while num_of_badTries < 6:
        letterGuessed = input("Guess a letter: ")
        letterGuessed = letterGuessed.lower()
        isvValidInput = try_update_letter_guessed(letterGuessed, old_letters_guessed)
        if isvValidInput:
            if check_letter(secret_word, letterGuessed):
                show_hidden_word(secret_word , old_letters_guessed)
                num_of_goodTries = num_of_goodTries + 1
                if check_win(secret_word , old_letters_guessed):
                    print ("WIN")
                    break
            else:
                num_of_badTries = num_of_badTries + 1
                print_hangman(num_of_badTries + 1)
                show_hidden_word(secret_word, old_letters_guessed)
                if num_of_badTries == 6:
                    print("LOSE")
                    break
                    

if __name__ == "__main__":
    main()
