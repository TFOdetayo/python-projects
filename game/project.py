# A code that prints whether a year is a leap year
# A code that suggests a nick name

import random
#import string

def nick_name():
    suffixes = ["pie", "cake", "berry", "sweet", "baby", "love", "jewelry", "smart", "test"]
    user_name = input("What should I call you? ")
    user_name_upper = []
    user_name_upper.append(user_name[:1].upper() + user_name[1:])
    user_name_upper = "".join(user_name_upper)
    print("Hello, "+user_name_upper+"!\nShould I suggest a sweet nickname for you?")
    answer = input("Enter Yes or No: ")

    if answer in ("Yes", "yes", "YES", "Y", "y"):
        new_name = []

        new_name.append(user_name_upper[:3] + random.choice(suffixes))
        new_name = "".join(new_name)
        print("I think "+new_name+" sounds cool. Let's see how good you are with madlibs, "+new_name+"!") #"Do you like it or want to create your own?"
    else:
        print("Okay, Let's see how good "+user_name_upper+" is with madlibs!")

    print(" ")
    madlibs()

# def user_name():
#     user_name = input("What should I call you? ")
#     user_name_upper = []
#     user_name_upper.append(user_name[:1].upper() + user_name[1:])
#     user_name_upper = "".join(user_name_upper)

def madlibs():
        print("Welcome to Taiwo's Madlibs\nHint: Psalm 23.")
        noun1 = input("Enter a noun: ")
        noun2 = input("Enter another noun: ")
        noun3 = input("Enter another noun: ")
        noun4 = input("Enter another noun: ")
        noun5 = input("Enter another noun: ")
        noun6 = input("Enter another noun: ")
        noun7 = input("Enter another noun: ")
        noun8 = input("Enter another noun: ")
        noun9 = input("Enter another noun: ")
        verb1 = input("Enter a verb: ")
        verb2 = input("Enter another verb: ")
        verb3 = input("Enter another verb: ")
        verb4 = input("Enter another verb: ")
        verb5 = input("Enter another verb: ")
        plural_noun1 = input("Enter a plural noun: ")
        active_verb1 = input("Enter an active verb: ")
        active_verb2 = input("Enter another active verb: ")
        pronoun1 = input("Enter a pronoun: ")
        conjunction1 = input("Enter a conjunction: ")
        conjunction2 = input("Enter another conjunction: ")
        preposition1 = input("Enter a preposition: ")
        adverb1 = input("Enter an adverb: ")
        adverb2 = input("Enter another adverb: ")
        your_name = input("Remind me your name.. ")

        madlib = f"The Lord is my {noun1}, I shall not {verb1}. He makes {your_name} to lie down in green {plural_noun1}. He {active_verb1} me beside the still waters. He {active_verb2} my {noun2}. He leads me in the paths of {noun3} for His name's {noun4}. Yeah, {conjunction1} I walk {preposition1} the {noun5} of the {noun6} of death, I shall {verb2} no evil. For You are with {your_name}, Your {noun7}, and Your staff, they {verb3} {your_name}. You prepare a table {adverb1} {your_name} in the {noun8} of my enemies. You {verb4} my head with oil, my cup runs {adverb2}. Surely, goodness {conjunction2} mercy {pronoun1} following {your_name}, all the {noun9} of my life, and I will {verb5} in the house of the Lord, {adverb2}. Amen."

        print(madlib)
#madlib = print("The Lord is my Shepherd, I shall not want. He makes me to lie down in green pasture. He leads me beside the still waters. He restores my soul. He leads me in the paths of righteousness for His name's sake. Yeah, though I walk through the valley of the shadow of death, I shall fear no evil. For You are with me, Your rod, and Your staff, they comfort me. You prepare a table before me in the presence of my enemies. You anoint my head with oil, my cup runs over. Surely, goodness and and mercy are following me, all the days of my life, and I will dwell in the house of the Lord, forever. Amen.")

        #"""user_create_name = input("Yes or continue? ")
        # user_create = True
        #if user_create_name in ("Yes", "yes", "YES", "Y", "y"):
            #user_input_name = input("Enter your favourite nickname. ")
            #while user_create:
                # try:
                #     if user_input_name == string.ascii_letters(user_input_name):
                #         print("I think "+user_input_name+" sounds cool.")
                # except TypeError:
                #     pass
                #     user_input_name = input("Oops! I didn't understand that. Please enter a letter of the alphabet. ")
                    #user_create = False
        #else:
            #print("Okay! Let's continue.")"""

nick_name()

# """def leap_year():
#     year = int(input("Enter the year you were born: "))
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("You were born in a leap year")
#             else:
#                 print("You were not born in a leap year")
#         else:
#             print("You were born in a leap year")
#     else:
#         print("You were not born in a leap year")

# leap_year()"""