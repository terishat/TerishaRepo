# Terisha Theodat
# This program is a music quiz that reveals what type of singer the user is and gives recommendations of the type of music the user would sing well.

print("Hi there! \nLooking for a fun quiz to play? Look no further ;)")
name = input("Please enter your name: ")
print(name, "take this quiz and find out what type of singer you are~", sep=', ')
play = input("Enter the letter *p* to get started -> ")

###QUIZ###
#################################QUESTION 1 - 3 (numerical questions)
def quiz_questions():
    score = 1  # score that user begins with
    try:
        print("\nQuestion #1")
        first_answer = int(float(input(
            "On a scale of 1 (can't hit at all) to 5 (next mariah carey), how well are you at hitting high notes? ")))
        if (first_answer > 0 and first_answer < 6):  # checks if *second_answer* is an integer between 1 and 5
            # depending on value of *first_answer* the user's score will be multiplied by *first_answer*
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
            score -= 1
            print("STRIKE 1: Not a number from 1 to 5 :(")
        print("Your score so far:", score,
              end=" points")  # how to use end= @ https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

        print("\n\nQuestion #2")
        second_answer = int(float(input(
            "On a scale of 1 (sound like a dying frog) to 5 (very skilled), how skilled are you at hitting low notes? ")))
        if (second_answer > 0 and second_answer < 6):  # checks if *second_answer* is an integer between 1 and 5
            # depending on value of *second_answer* the user's score will be raised to the power of *second_answer*
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
            score -= 2
            print("STRIKE 2: Not a number from 1 to 5 :(")
        print("Your score so far:", score,
              end=" points")  # how to use end= @ https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

        print("\n\nQuestion #3")
        third_answer = int(float(input("How many octaves can you sing? ")))
        # depending on *third_answer* the user's score is evenly divided by *third_answer*, and this result is added back to the user's score.
        if (third_answer > 0 and third_answer < 6):
            score += (score // third_answer)
            for time in range(0, third_answer + 1):
                for col in range(time):
                    print("WOW!!!", end="")
                print()
                # Professor Osheroff's POGIL 10 Nested Loops
                # prints *wow!!!* to congratulate user for their vocal range
        else:
            score -= 3
            if (score == -5):
                print(
                    "STRIKE 3! READ QUESTIONS CAREFULLY!!!" * 3)  # prints *strike 3!* 3 times to let user know that they have too many invalid inputs
            else:
                print("STRIKE! " * 3)  # prints *strike 3!* 3 times to let user know that their answer was invalid
        print(numerical_answers(score))

        #################################QUESTION 4 - 6 (a, b, c questions)
        print("\n\nQuestion 4")
        print("How much control do you have over your voice when singing (a, b, c)?: ")
        print("a) A lot of control")
        print("b) Some control")
        print("c) Little to no control")
        fourth_answer = input()

        print("\n\nQuestion 5")
        print("Is your singing voice too soft, too loud, or just the right volume (a, b, c)?: ")
        print("a) just right")
        print("b) too loud")
        print("c) too soft")
        fifth_answer = input()

        print("\n\nQuestion 6")
        print("Do you have a strong, average, or weak singing voice (a, b, c)?: ")
        print("a) strong")
        print("b) average")
        print("c) weak")
        sixth_answer = input()

        print(short_answers(score, fourth_answer, fifth_answer, sixth_answer))

    except:
        print("STOP")


#################################QUESTIONS 1 - 3 SCORE EVALUATION
def numerical_answers(user_score):
    if (user_score >= 128):  # if the user had inputted at least 4, 4, 2 for their answers
        return "\nSo far you are showing a great range! Your score so far is " + str(user_score)
    elif (user_score != 1 or user_score != 0):
        return "\nYour range is pretty decent, but it can be improved. Your score so far is " + str(user_score)
    else:
        return "\nYour range could use some work. Your score so far is " + str(user_score)


#################################QUESTIONS 4 - 6 SCORE EVALUATION
def short_answers(user_score, answer_four, answer_five, answer_six):
    user_answers = [answer_four, answer_five, answer_six]
    count_A = 0
    count_B = 0
    count_C = 0
    for answer in user_answers:
        if (answer >= 'a' and answer <= 'c'):
            if (answer == 'a'):
                user_score = user_score % 2
                count_A += 1
            elif (answer == 'b'):
                user_score = user_score % 3
                count_B += 1
            else:
                user_score = user_score % 7
                count_C += 1
        else:
            user_score = user_score / 10
    if (count_A >= 2):
        return "\nYou have an awesome singing voice that is pretty strong, that projects at the right volume, and/ or has a lot of control! That's amazing!!!"
    elif (count_B >= 2):
        return "\nYou either have decent control of your voice, a volume that can be heard, or decent strength in your voice! Strengthen your strengths and work on your weaknesses ;)"
    elif (count_C >= 2):
        return "\nYou could use some improvement in the control, soft volume, and/or strength of your singing voice. Don't give up & but don't go overboard with it haha!"
    else:
        return "\nYour score as of now is " + str(user_score)


while (play == 'p'):
    quiz_questions()  ################# MAIN FUNCTION #################
    play = input("Enter any key BESIDES *p* to quit OR enter *p* to keep playing -> ")

if (not (play == 'p')):  ################# if user does not press *p* to play, then they are exitted out of the quiz
    print("Bye, " + name)
