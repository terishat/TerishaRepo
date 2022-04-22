"""My Integration Program: Music Quiz!"""
__author__ = "Terisha Theodat"


def main():
    """
    This program is a music quiz that reveals what type of singer the user is
    and gives recommendations of the type of music the user would sing well.
    """
    print("\nHi there! \nLooking for a fun quiz to play? Look no further ;)")
    name = input("Please enter your name: ")
    print(name, "take this quiz and find out what type of singer you are~",
          sep=', ')
    quiz_questions(name)


def quiz_questions(user_name):
    """
    The following function asks the user questions about their singing skills
    and calculates their scores along the way
    :param user_name:
    """
    validating_the_input = True  # this variable is always True until all of the
    # quiz questions are answered in order to keep going thru the quiz even
    # when an incorrect input is given
    while (validating_the_input == True):
        score = 1  # score that user begins with
        try:
            # QUESTIONS 1 - 3 (numerical questions)
            print("\nQuestion #1")
            first_answer = int(float(input(
                "On a scale of 1 (can't hit at all) to 5 (next mariah carey), "
                "how well are you at hitting high notes? ")))
            if (first_answer > 0 and first_answer < 6):  # checks if
                # *second_answer* is an integer between 1 and 5
                # depending on value of *first_answer* the user's score
                # will be multiplied by *first_answer*
                if (first_answer == 1):
                    score *= 1
                elif (first_answer == 2):
                    score *= 2
                elif (first_answer == 3):
                    score *= 3
                elif (first_answer == 4):
                    score *= 4
                else:
                    score *= 5
            else:
                # If the answer entered is not between one and six an
                # exception is raised.
                raise ValueError  # https://docs.python.org/3/tutorial/errors.html

            print("\n\nQuestion #2")
            second_answer = int(float(input(
                "On a scale of 1 (sound like a dying frog) to 5 (very skilled),"
                " how skilled are you at hitting low notes? ")))
            if (second_answer > 0 and second_answer < 6):  # checks if
                # *second_answer* is an integer between 1 and 5
                # depending on value of *second_answer* the user's
                # score will be raised to the power of *second_answer*.
                if (second_answer == 1):
                    score = score ** 1
                elif (second_answer == 2):
                    score = score ** 2
                elif (second_answer == 3):
                    score = score ** 3
                elif (second_answer == 4):
                    score = score ** 4
                else:
                    score = score ** 5
            else:
                # If the answer entered is not between one and six an
                # exception is raised.
                raise ValueError  # https://docs.python.org/3/tutorial/errors.html

            print("\n\nQuestion #3")
            third_answer = int(float(input("How many octaves can you sing? "
                                           "\n***TIP: Find how many octaves "
                                           "you can sing by counting the "
                                           "total number of notes between "
                                           "your highest and lowest pitches"
                                           " as sets of seven.\n Octaves: ")))
            # depending on *third_answer* the user's score is evenly divided
            # by *third_answer*, and this result is added back to the user's
            # score.
            if (third_answer > 0 and third_answer < 6):
                score += (score // third_answer)
                for time in range(0, third_answer + 1):
                    for col in range(time):
                        print("WOW!!!", end="")
                    print()
                    # Professor Osheroff's POGIL 10 Nested Loops
                    # prints *wow!!!* to congratulate user for their vocal
                    # range
            else:
                # If the answer entered is not between one and six an
                # exception is raised.
                raise ValueError  # https://docs.python.org/3/tutorial/
                # errors.html
            print(numerical_answers(score))

            # QUESTIONS 4 - 6 (a, b, c questions)
            print("\n\nQuestion 4")
            print("How much control do you have over your voice when singing "
                  "(a, b, c)?: ")
            print("a) A lot of control")
            print("b) Some control")
            print("c) Little to no control")
            fourth_answer = input()
            # If the answer entered is not a, b, or c an exception is raised.
            if(fourth_answer != 'a' and fourth_answer != 'b' and
                    fourth_answer != 'c'):
                raise UnboundLocalError  # https://docs.python.org/3/
                # tutorial/errors.html

            print("\n\nQuestion 5")
            print("Is your singing voice too soft, too loud, or just the "
                  "right volume (a, b, c)?: ")
            print("a) just right")
            print("b) too loud")
            print("c) too soft")
            fifth_answer = input()
            # If the answer entered is not a, b, or c an exception is raised.
            if (fifth_answer != 'a' and fifth_answer != 'b' and
                    fifth_answer != 'c'):
                raise UnboundLocalError  # https://docs.python.org/3/
                # tutorial/errors.html

            print("\n\nQuestion 6")
            print("Do you have a strong, average, or weak singing voice "
                  "(a, b, c)?: ")
            print("a) strong")
            print("b) average")
            print("c) weak")
            sixth_answer = input()
            # If the answer entered is not a, b, or c an exception is raised.
            if (sixth_answer != 'a' and sixth_answer != 'b' and
                    sixth_answer != 'c'):
                raise UnboundLocalError  # https://docs.python.org/3/
                # tutorial/errors.html

            print(short_answers(score, fourth_answer, fifth_answer,
                                sixth_answer))
            validating_the_input = False  # Setting validating_the_input to
            # False to stop the while loop.
            exit_quiz(user_name)  # Calling the function that lets users exit
            # the program once the quiz is finished.

        except ValueError:
            print("ERROR: Please enter an integer between 1 and 5 (inlcuding"
                  " 1 and 5)... Starting over...")
        except UnboundLocalError:
            print("ERROR: Please enter 'a', 'b' or 'c'... Starting over...")


def numerical_answers(user_score):
    """
    This function receives the results from questions one through three
    on the quiz questions, and evaluates the user's singing range and displays
    their current scores depending on theuser's answers.
    :param user_score:
    :return:
    """
    if (user_score >= 128):  # if the user had inputted at least 4, 4, 2 for
        # their answers
        return "\nSo far you are showing a great range! Your score so far is " \
               + str(user_score)
    elif (user_score != 1 or user_score != 0):
        return "\nYour range is pretty decent, but it can be improved. Your" \
               " score so far is " + str(user_score)
    else:
        return "\nYour range could use some work. Your score so far is " \
               + str(user_score)


def short_answers(user_score, answer_four, answer_five, answer_six):
    """
    This function receives the results from questions four through six
    on the quiz questions, and returns a tip for singing depending on the
    user's answers.
    :param user_score:
    :param answer_four:
    :param answer_five:
    :param answer_six:
    :return:
    """

    # The users' answers to questions four through six are saved in an array.
    # Each element in the array is checked to see how many times the user
    # entered 'a', 'b', and 'c'
    user_answers = [answer_four, answer_five, answer_six]
    count_a = 0
    count_b = 0
    count_c = 0
    for answer in user_answers:
        if (answer >= 'a' and answer <= 'c'):
            if (answer == 'a'):
                user_score = user_score % 2
                count_a += 1
            elif (answer == 'b'):
                user_score = user_score % 3
                count_b += 1
            else:
                user_score = user_score % 7
                count_c += 1
        else:
            user_score = user_score / 10

    # Depending on whether the user answered 'a', 'b', or 'c' more frequently,
    # a singing tip and songs tailored to their singing skills are returned.
    if (count_a >= 2):
        return "\nYou have an awesome singing voice that is pretty " \
               "strong, that projects at the right volume, and/ or has " \
               "a lot of control! That's amazing!!!\nTry singing " \
               "songs like *Stone Cold* by Demi Lovato or " \
               "*I Have Nothing* by Whitney Houston to " \
               "further strengthen your talent."
    elif (count_b >= 2):
        return "\nYou either have decent control of your voice, a volume " \
               "that can be heard, or decent strength in your voice!" \
               " Strengthen your strengths and work on your weaknesses ;)" \
               " \nTry singing songs like *No Time to Die* by Billie " \
               "Eilish or *We Belong Together* by Mariah Carey to help " \
               "you vary your voice control and vocal strength."
    elif (count_c >= 2):
        return "\nYou could use some improvement in the control, soft " \
               "volume, and/or strength of your singing voice. Don't give" \
               " up & but don't go overboard with it haha! \nTry" \
               " singing songs like *Just the Way You Are* by Bruno" \
               " Mars to strengthen your weaknesses."
    else:
        return "\nEither you're a little bit of everything or you're " \
               "not sure about your vocal capabilities. \nTry singing " \
               "fun songs like *Rather Be* by Clean Bandit!"


def exit_quiz(user):
    """
    This function asks the user if they would like to play the quiz again
    or if they would like to exit the quiz. If the user enters "p", then
     the quiz is repeated, else the user exits the quiz.
    :param user:
    """
    play = input("\nThanks for playing! I hope you enjoyed it! Press any "
                 "key BESIDES *p* to exit the quiz OR enter *p* to play"
                 " again -> ")
    if (not (play == 'p')):
        # if user does not enter
        # *p*, then they exit the program
        print("Bye, " + user)
    else:
        main()


# # call to main function
if __name__ == "__main__":
    main()
