#Hi! This is my project for the 'Code Your Own Quiz' section from Udacity's 'Intro to Programming' Nanodegree. I hope you like it!


#list of the numbered blanks that are to be replaced.
numbered_blanks = ["__1__", "__2__", "__3__", "__4__"]

#lists for the correct answers for each level of difficulty.
easy_solutions = ["9", "16", "36", "49"]
medium_solutions = ["121", "196", "256", "361"]
hard_solutions = ["529", "625", "784", "527" ]

#master list to be able to choose different solution lists.
solutions = [easy_solutions, medium_solutions, hard_solutions]

#text for each level of difficulty.
easy_text = """3 x 3 = __1__ ///// 4 x 4 = __2__ ///// 6 x 6 = __3__ ///// 7 x 7 = __4__"""
medium_text = """11 x 11 = __1__ ///// 14 x 14 = __2__ ///// 16 x 16 = __3__ ///// 19 x 19 = __4__"""
hard_text = """23 x 23 = __1__ ///// 25 x 25 = __2__ ///// 28 x 28 = __3__ ///// 31 x 17 = __4__"""

#master list to be able to choose the different texts.
texts = [easy_text, medium_text, hard_text]

#lets the user select a level of difficulty.
#Input: level of difficulty.
#Output: passes that level on to the quiz function.
def choose_difficulty():
    user_input_choose_difficulty = raw_input("\nHi! Welcome to my quiz!" + ("\n"*2) + "Please select a game difficulty by typing it in!\nPossible choices include easy, medium and hard.\n")
    levels = ["easy", "medium", "hard"]
    if user_input_choose_difficulty in levels:
        quiz(levels.index(user_input_choose_difficulty))
    else:
        print "That's not a valid input!"
    print ("\n"*3) + "GAME OVER" + ("\n"*10)
#Lets the user input a preferred number of wrong guesses allowed. Then lets the user play the game.
#Asks for answer, the user types his guess in, checks that answer and either says and tells the user
#whether the answer is correct or false. If correct, the correct answer is integrated in the quiz text.
#Input: a level of difficulty selected by the user in choose_difficulty() and the users guesses.
#Output: win/loose statement.
def quiz(level_of_difficulty):
    text = texts[level_of_difficulty]
    index = int(raw_input(("\n"*2) + "How many trys do you want to have per problem?\n"))
    last_try = 0
    index_answers_blanks = 0
    while index > last_try and index_answers_blanks < len(numbered_blanks):
        user_input_1 = raw_input(("\n"*2) + "This is what the quiz currently looks like:" + ("\n"*2) + text + ("\n"*2) + "What is " + str(numbered_blanks[index_answers_blanks]) + " ?\n")
        if user_input_1 == solutions[level_of_difficulty][index_answers_blanks]:
            text = insert_correct_answers(text, numbered_blanks, solutions[level_of_difficulty][index_answers_blanks], numbered_blanks[index_answers_blanks] )
            index_answers_blanks += 1
            print ("\n"*2) + "Correct!"
            if index_answers_blanks == len(numbered_blanks):
                print ("\n"*10) + "Congratulations! You win!"
        else:
            index -= 1
            if index > last_try:
                print ("\n"*2) + ("False! You have " + str(index) +" trys left! Try again!")
            elif index == last_try:
                print ("\n"*10) + "False! You have no more trys left!"


# Checks if a word in list_of_placeholders is a substring of the word passed in.
def word_in_placeholder(word, list_of_placeholders):
    for shared_part in list_of_placeholders:
        if shared_part in word:
            return shared_part
    return None

#Replaces certain_placeholders in text_by_difficulty, which appear in
#list_of_placeholders and text_by_difficulty with correct_answers.
def insert_correct_answers(text_by_difficulty, list_of_placeholders, correct_answer, certain_placeholder):
    replaced = []
    text_by_difficulty = text_by_difficulty.split()
    for word in text_by_difficulty:
        replacement = word_in_placeholder(word, list_of_placeholders)
        if replacement == str(certain_placeholder):
            word = word.replace(replacement,correct_answer)
            replaced.append(word)
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

#for calling the function:
choose_difficulty()
