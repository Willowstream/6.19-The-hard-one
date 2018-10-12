def get_num_of_non_WS_characters(user_string):
    # create a variable that will act as a sort of counter
    # for non-whitespace characters
    non_ws_characters = 0

    # iterate over user_string and add 1 to non_ws_characters
    # if the loop variable != ' '
    for characters in user_string:
        if characters != ' ':
            non_ws_characters += 1
        else:
            continue

    # return the number of non-whitespace characters
    return non_ws_characters
# non-whitespacing = done
def get_num_of_words(user_string):
    words = 0
    # count the words
    for character in user_string:
        if character == ' ':
            words += 1

    # add the last word
    words += 1

    # return the number of words
    return words
#word counting = done
def fix_capitalization(user_string):
    corrections = 0
    string_two = ''
    string_three = ''
    sentence_end = 0

    # correct the first character in the string if necessary
    if user_string[0].islower():
        string_two += user_string.capitalize()
        corrections += 1

    # fix the capitalization and make a count of the fixes
    for character in string_two:
        if (sentence_end == 1) and (character != ' '):
            if character.islower():
                string_three += character.upper()
                corrections += 1
                sentence_end = 0
        else:
            string_three += character

        if (sentence_end == 0) and (character == ' '):
            space = 1

        if (character == '.') or (character == '!') or (character == '?'):
            sentence_end = 1

    return string_three, corrections

def replace_punctuation(user_string):
    # declare needed variables
    modified_string = ''
    ex_corrections = 0
    semi_corrections = 0

    # replace exclamation points and semi-colons with periods and commas respectively
    for (index, character) in user_string:
        if character == '!':
            modified_string += '.'
            ex_corrections += 1
        elif character == ';':
            modified_string += ','
            semi_corrections += 1
        else:
            modified_string += character

    # return the results
    return modified_string, ex_corrections, semi_corrections

def shorten_space(user_string):
    modified_string = ''
    spaces = 0

    for character in user_string:
        if character == ' ':
            spaces += 1

        if spaces >= 2:
            modified_string += ' '
        else:
            modified_string
    return modified_string

def print_menu(user_string):
    string = user_string
    print("MENU")
    print("c - Number of non-whitespace characters")
    print("w - Number of words")
    print("f - Fix capitalization")
    print("r - Replace punctuation")
    print("s - Shorten spaces")
    print("q - Quit")
    print()

    # prompt for the option
    menu_option = input("Choose an option:\n")

    while menu_option != 'q':
        if menu_option == 'q':
            print('Quitting')
        elif menu_option == 'c':
            output = get_num_of_non_WS_characters(string)
            print('Number of non-whitespace characters:', output)
            print()
        elif menu_option == 'w':
            output = get_num_of_words(string)
            print('Number of words:', output)
        elif menu_option == 'f':
            output, corrections = fix_capitalization(string)
            print('Number of letters capitalized:', corrections)
            print('Edited text:', output)
            string = output
        elif menu_option == 'r':
            output, ex_count, semi_count = replace_punctuation(string)
            print('exclemationCount:', ex_count)
            print('semicolonCount:', semi_count)
            print('Edited text:', output)
        elif menu_option == 's':
            output = shorten_space(string)
            print('Edited text:', output)
            string = output

            # print the results
            print('')

        print("MENU")
        print("c - Number of non-whitespace characters")
        print("w - Number of words")
        print("f - Fix capitalization")
        print("r - Replace punctuation")
        print("s - Shorten spaces")
        print("q - Quit")

        print()

        menu_option = input("Choose an option:\n")

    return

user_string = input('Enter a sample text:\n')
print()
print('You entered:', user_string)
print()

print_menu(user_string)
