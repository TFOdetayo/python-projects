# In this game, I want the player to be able to select difficulty level
# and at each level, shuffle the madlibs

import random
import time

suffixes = ["pie", "cake", "berry", "omalecha", "bebe", "ajoke", "adunni", "babym", "sweetim", "baby", "love", "jewelry", "smart", "test"]
# These are the suffixes that make the nick names
user_name = ''
user_name_upper = []

def start(): # this one holds the stages of the codes
    global user_name
    user_name = input("Welcome! What should I call you? ")
    upper_name() # this is where the first letter of the user input gets converted to uppercase
    while madlib(): # this is the game
        pass

def madlib():
    selectLevel() # we select difficulty level
    return play_again() # the user can choose to play again

def upper_name():
    global user_name
    global user_name_upper
    user_name_upper = []
    user_name_upper.append(user_name[:1].upper() + user_name[1:]) # I cut the input to remain only the first letter
    user_name_upper = "".join(user_name_upper)
    print("Hello, "+user_name_upper+"!\nShould I suggest a sweet nickname for you?")
    answer = input("Enter Yes or No: ")

    if answer in ("Yes", "yes", "YES", "Y", "y"):
        suggest_nickname()
    else:
        print("Okay, let's see how good you are with madlibs, "+user_name_upper+"!")

    print(" ")

def suggest_nickname():
    global user_name_upper
    new_name = []
    new_name.append(user_name_upper[:3] + random.choice(suffixes))
    new_name = "".join(new_name)
    print("I think "+new_name+" sounds cool.")
    print("Let's see how good you are with madlibs, "+new_name+"!")
    #"Do you like it or want to create your own?"

def selectLevel():
    time.sleep(0.8)
    level = int(input("Select Level\n\nEasy: Press 1\nMedium: Press 2\nHard: Press 3 \n "))

    if level == 1:
        print("You chose Easy level\n")
        time.sleep(0.8)
        madlibs_easy()
    elif level == 2:
        print("You chose Medium level\n")
        time.sleep(0.8)
        madlibs_medium()
    elif level == 3:
        print("You chose Hard level\n")
        time.sleep(0.8)
        madlibs_hard()
    else:
        print("Oops, I didn't understand that! Select level again.")
        level = int(input("Select Level\nEasy: Press 1\nMedium: Press 2\nHard: Press 3 \n ")) 

def compilation():
    time.sleep(0.3)
    print("Compiling your answers...")
    time.sleep(0.5)

def play_again():
    again = input("Would you like to play again? Yes or No: ")
    if again in ("yes", "Yes", "y", "Y", "sure"):
        return again
    print("Thank you for taking the challenge")

def madlibs_easy():
    easylevel = [inlove, favjob, holiday]
    return (random.choice(easylevel)())

def madlibs_medium():
    mediumlevel = [mymother, twinkle]
    return (random.choice(mediumlevel)())

def madlibs_hard():
    hardlevel = [psalm23, psalm24]
    return (random.choice(hardlevel)())
    # random.shuffle(hardlevel)
    # hardlevel[0]()
    # hardlevel[1]()
    # hardlevel[2]()

def inlove():
    print("Welcome to Taiwo's Easy level Madlib. Hint: My Friend.")
    verb1 = input("Enter a verb: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    friends_name = input("Enter your best friend's name: ")
    compilation()

    madlib = f"Well, we {verb1} in a world where {noun1} fall in love with one another. So, it is not a {noun2} that I am in love with {friends_name}."

    print(madlib)

def favjob():
    print("Welcome to Taiwo's Easy level Madlib. Hint: My favourite work.")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    hobby = input("Enter your hobby: ")
    compilation()

    madlib = f"I love {hobby}. It makes me feel {adjective1} of myself when I am able to offer {noun1} to problems in our {noun2}."

    print(madlib)

def holiday():
    print("Welcome to Taiwo's Easy level Madlib. Hint: My holiday.")
    adverb1 = input("Enter an adverb: ")
    verb1 = input("Enter a verb: ")
    noun1 = input("Enter a noun: ")
    fav_meat = input("Enter your favourite meat: ")
    fav_swallow = input("Enter your favourite swallow: ")
    fav_stew = input("Enter your favourite stew: ")
    compilation()

    madlib = f"I {adverb1} want to go and {verb1} my Easter {noun1} at home. Eating {fav_meat} and swallowing {fav_swallow} and {fav_stew} with my family."

    print(madlib)

def mymother():
    print("Welcome to Taiwo's Medium level Madlib. Hint: My Mother.")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter another verb: ")
    verb4 = input("Enter another verb: ")
    verb5 = input("Enter another verb: ")
    adjective1 = input("Enter an adjective: ")
    continuous_verb = input("Enter a continuous verb: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    noun4 = input("Enter another noun: ")
    adverb1 = input("Enter an adverb: ")
    adverb2 = input("Enter another adverb: ")
    number = input("Enter a number: ")
    fav_person = input("Enter the name of a perfect one: ")
    compilation()

    madlib = f"Who {verb1} and {verb2} my {adjective1} head, while {continuous_verb} on my cradle {noun1}. And tears of sweet {noun2} shed. My mother! Day by {noun3}, dear Lord these {number} things I {verb3}, to see thee more {adverb1}, {verb4} thee more {adverb2}, {verb5} {fav_person} more nearly, {noun4} by {noun4}."

    print(madlib)

def twinkle():
    print("Welcome to Taiwo's Medium level Madlib. Hint: Twinkle twinkle little stars.")
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    adverb1 = input("Enter an adverb: ")
    adverb2 = input("Enter another adverb: ")
    fav_gem = input("Enter the name of your favourite stone: ")
    fav_machineoftransport = input("Enter the name of your favourite automobile: ")
    water_body = input("Enter the name of a waterbody: ")
    adverbofenjoyment = input("Enter an adverb of enjoyment: ")
    kitchen_equipment = input("Enter the name of your favourite kitchen utensil: ")
    compilation()


    madlib = f"Twinkle, {adjective1} little {noun1}, how I {verb1} what you are! Up {adverb1} the sky so {adverb2}, like a {fav_gem} in the sky. Roll {verb2} your {fav_machineoftransport}, gently on the {water_body}. Merrily {adverbofenjoyment} merrily, life is but a {kitchen_equipment}."

    print(madlib)

def psalm23():
    global user_name_upper
    print("Welcome to Taiwo's Hard level Madlib. Hint: Psalm 23.")
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
    your_name = user_name_upper
    compilation()

    madlib = f"The Lord is my {noun1}, I shall not {verb1}. He makes {your_name} to lie down in green {plural_noun1}. He {active_verb1} me beside the still waters. He {active_verb2} my {noun2}. He leads me in the paths of {noun3} for His name's {noun4}. Yeah, {conjunction1} I walk {preposition1} the {noun5} of the {noun6} of death, I shall {verb2} no evil. For You are with {your_name}, Your {noun7}, and Your staff, they {verb3} {your_name}. You prepare a table {adverb1} {your_name} in the {noun8} of my enemies. You {verb4} my head with oil, my cup runs {adverb2}. Surely, goodness {conjunction2} mercy {pronoun1} following {your_name}, all the {noun9} of my life, and I will {verb5} in the house of the Lord, {adverb2}. Amen."

    print(madlib)

def psalm24():
    print("Welcome to Taiwo's Hard level Madlib. Hint: Psalm 24.")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter another noun: ")
    noun3 = input("Enter another noun: ")
    noun4 = input("Enter another noun: ")
    noun5 = input("Enter another noun: ")
    noun6 = input("Enter another noun: ")
    noun7 = input("Enter another noun: ")
    noun8 = input("Enter another noun: ")
    noun9 = input("Enter another noun: ")
    noun10 = input("Enter another noun: ")
    noun11 = input("Enter another noun: ")
    noun12 = input("Enter another noun: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter another verb: ")
    verb3 = input("Enter another verb: ")
    verb4 = input("Enter another verb: ")
    verb5 = input("Enter another verb: ")
    pastparticiple1 = input("Enter a past participle: ")
    pastparticiple2 = input("Enter another past participle: ")
    pastparticiple3 = input("Enter another past participle: ")
    pronoun1 = input("Enter a pronoun: ")
    pronoun2 = input("Enter another pronoun: ")
    adverb1 = input("Enter an adverb: ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    compilation()

    madlib = f"The {noun1} is the Lord's, and the {noun2} thereof; the world, and they that {verb1} therein. He has {pastparticiple1} it upon the {noun3}, and has {pastparticiple2} it upon the {noun4}. Who {pronoun1} {verb2} into the {noun5} of the Lord? Or who shall {verb3} in His {adjective1} place? He that has {adjective2} hands, and a pure {noun6}; who has not {pastparticiple3} up his {noun7} to vanity, nor sworn {adverb1}. He shall {verb4} the {noun8} from the Lord, and {noun9} from the God of his {noun10}. This is the {noun11} of {pronoun2} that {verb5} him, that seek thy {noun12}, O Jacob, Selah."

    print(madlib)

    madlib = f"Reading is so fun, I love to spend my time looking at my books and seeing the letters mske wordds tha "

# madlib = f"The Lord is my Shepherd, I shall not want. He makes me to lie down in green pasture. He leads me beside the still waters. He restores my soul. He leads me in the paths of righteousness for His name's sake. Yeah, though I walk through the valley of the shadow of death, I shall fear no evil. For You are with me, Your rod, and Your staff, they comfort me. You prepare a table before me in the presence of my enemies. You anoint my head with oil, my cup runs over. Surely, goodness and and mercy are following me, all the days of my life, and I will dwell in the house of the Lord, forever. Amen."

# madlib = f"The earth is the Lord's, and the fullness thereof; the world, and they that dwell therein. He has founded it upon the seas, and has established it upon the floods. Who shall ascend into the hill of the Lord? Or who shall stand in His holy place? He that has clean hands, and a pure heart; who has not lifted up his soul to vanity, nor sworn deceitfully. He shall receive the blessing from the Lord, and righteousness from the God of his salvation. This is the generation of them that seek him, that seek thy face, O Jacob, Selah."


# madlib = f"Well, we live in a world where humans fall in love with one another. So, it is not a surprise that I am in love with Tychicus."

# madlib = f"I love coding. It makes me feel proud of myself when I am able to offer solutions to problemsin our world."

# madlib = f"I really want to go and spend my Easter holiday at home. Eating  meat and swallowing Amala and ewedu with my family."

# madlib = f"Who sat and watched my infant head, while sleeping on my cradle bed. And tears of sweet affcetion shed. My mother! Day by day, dear Lord these three things I pray, to see thee more clearly, love thee more dearly, follow thee more nearly. Day by day."

# madlib = f"Twinkle, twinkle little stars, how I wonder what you are! Up above the sky so high, like a diamond in the sky. Roll roll your boat, gently in the sea. Merrily merrily merrily, life is but a dream."

start()
