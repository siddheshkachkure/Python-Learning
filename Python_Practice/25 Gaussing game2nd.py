import random

MINIMUM = 0
MAXIMUM = 100
NUMBER = random.randint(MINIMUM, MAXIMUM)
TRY = 0
RUNNING = True
ANSWER = None

while RUNNING:
    print("Is it %s?" % str(NUMBER))
    ANSWER = raw_input()
    if "no" in ANSWER.lower() and "lower" in ANSWER.lower():
        NUMBER -= random.randint(1, 4)
    elif "no" in ANSWER.lower() and "higher" in ANSWER.lower():
        NUMBER += random.randint(1, 4)
    elif ANSWER.lower() == "no":
        print("Higher or lower?")
        ANSWER = raw_input()
        if ANSWER.lower() == "higher":
            NUMBER += random.randint(1, 4)
        elif ANSWER.lower() == "lower":
            NUMBER -= random.randint(1, 4)
    elif ANSWER.lower() == "yes":
        if TRY < 2:
            print("Yes! It only took me %s try!" % str(TRY))
        elif TRY < 2 and TRY < 10:
            print("Pretty well for a robot, %s tries." % str(TRY))
        else:
            print("That's so bad, %s tries." % str(TRY))
        RUNNING = False
    TRY += 1
    
print("Thanks for the game!")