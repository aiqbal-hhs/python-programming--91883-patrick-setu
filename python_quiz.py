import time
import sys

try:
    colour = sys.stdout.shell
except AttributeError:
    raise RuntimeError("Use IDLE")

#BUILTIN = purple text
#SYNC = black text
#STRING = green text
#console = brown text
#COMMENT = red text
#KEYWORD = orange text
#stdout = blue text
#hit = white text, black background
#ERROR = black text, red background
#sel = black text, grey Background


#
#Green for 'true' and red for 'false' in questions


score = 0
num_questions = 0

print("Welcome to Patrick Pancho Setu's AS91883 Python Quiz! \n")

print("Each question is worth a point. Getting them right will earn more while incorrect answers will result in loss of points. Try and earn as many points as possible. The total points earned will be displayed at the end of the quiz. \n")
#set to 10s
time.sleep(0.1)

print("Some formulas that may be of use: \n"
    "velocity = d/t | acceleration = v/t | Force = ma | Power = W/t | Work = Fd")
time.sleep(3)

print("\nTip: You may refer to the formulas provided while answering the questions. \n")
time.sleep(3)

print("The quiz will begin in:")
time.sleep(1)

colour.write("3..","COMMENT")
time.sleep(1)

colour.write("\n2..","KEYWORD")
time.sleep(1)

colour.write("\n1..\n","STRING")
time.sleep(1)

print("\nThe quiz will now begin.")
time.sleep(1)

colour.write("\nQuestion One - Gravity","HIT")
num_questions += 1

print("\nThe acceleration of gravity is 10ms-1 for Level 1 mechanics.")

answer = input("\nTrue or false?").strip().lower()

if answer == "true":
    score += 1
elif answer == "false":
    score -= 1
else:
    while answer != "true" and answer != "false":
        print("\nNote: Enter an appropriate answer. \n")
        answer = input("True or false?").strip().lower()
        if answer == "true":
            score += 1
        elif answer == "false":
            score -= 1

print(score)
time.sleep(0.5)

print("\nQuestion Two - Work")
num_questions += 1

print("\nA box filled with heavy materials has a weight of 1500N. A forklift lifts the box upwards 2 metres. The forklift takes 10 seconds to lift the box. ")

#fix decimal problem caused by float
answer1 = int(float(input("\nCalculate the work done. (No units required)")))

if answer1 == 3000:
    score += 1
elif answer1 >= 10000:
    print("\nWoah there buddy. You're a bit too far off. \n"
    "Try again. \n")
    answer1 = int(input("Calculate the work done. (No units required)"))
    if answer1 == 3000:
        score += 1 
    else:
        score -= 1
elif answer1 <= 0:
    ("Hmm. I'm not quite sure that's possible. \n"
    "Try again. \n")
    while answer1 <= 0:
        answer1 = int(input("\nCalculate the work done. (No units required)"))
        if answer1 == 3000:
            score += 1
        else:
            score -= 1
else:
    score -= 1 

#Makes sure there isn't another correct answer option for the next question
if answer1 == 3000:
    answer1 += 4500 
elif answer1 >= 2998 and answer1 < 3000:
    answer1 = (answer1 * 0) + 7500
elif answer1 <= 3006 and answer1 > 3000:
    answer1 = (answer1 * 0) + 7500
    
print(score)    
time.sleep(0.5)

print("\nQuestion Three - Power")
num_questions += 1

print("\nUsing the answer from the previous question, what is the amount of power required to lift the box if it takes 10 seconds? \n"
    "A. {:.0f}W \n"
    "B. 450W \n"
    "C. 300W".format(answer1 / 10))
    
answer = input("\nIs the answer: A, B, or C?").strip().lower()

if answer == "a" or answer == "b":
    score -= 1
elif answer == "c":
    score += 1
else:
    print("\nNote: The only options are: A, B, or C. Select one of the available options.")
    while answer != "a" and answer != "b" and answer != "c":
        answer = input("\nIs the answer: A, B, or C?").strip().lower()
        if answer == "a" or answer == "b":
            score -= 1
        elif answer == "c":
            score += 1

print(score)
time.sleep(0.5)

print("\nQuestion Four - No work done")
num_questions += 1

print("\nThe forklift from Question 2 has now finished lifting the box upwards and now remains motionless.")

answer = input("\nIs there being work done after the 1500N box has been lifted for 10 seconds?").strip().lower()
if answer == "yes":
    score -= 1
elif answer == "no":
    score += 1
else:
    while answer != "yes" and answer != "no":
        print("\nNote: This is a yes or no question. Please answer as such.")
        answer = input("\nIs there being work done after the 1500N box has been lifted for 10 seconds?").strip().lower()
        if answer == "yes":
            score -= 1
        elif answer == "no":
            score += 1

print(score)
time.sleep(0.5)

print("\nQuestion Five - Mass and weight")
num_questions += 1

print("\nIn science, the mass of an object and the weight of an object are the same thing.")

answer = input("\nTrue or false?").strip().lower()

if answer == "true":
    score -= 1
elif answer == "false":
    score += 1
else:
    while answer != "true" and answer != "false":
        print("\nNote: Enter an appropriate answer. \n")
        answer = input("True or false?").strip().lower()
        if answer == "true":
            score -= 1
        elif answer == "false":
            score += 1

print(score)
time.sleep(1)


#fix float problem here as well
print("\nQuestion Six - Speed")
num_questions += 1

print("\nA truck is driving along the motorway. It travels 100 metres in the span of 5 seconds.")

answer = int(input("\nCalculate the speed of the truck. (No units required)"))

if answer == 20:
    score += 1
elif answer >= 0 and answer < 20:
    score -= 1 
elif answer > 20:
    score -= 1 
else:
    print("\nNot quite possible. Speed can't be negative.\n"
    "Try again.")
    while answer != 0 and answer < 0:
        answer = int(input("\nCalculate the speed of the truck. (No units required)"))
        if answer == 20:
            score += 1
        elif answer >= 0 and answer < 20:
            score -= 1 
        elif answer > 20:
            score -= 1
        else:
            print("\nNot quite possible. \n"
            "Try again.")
            answer = int(input("\nCalculate the speed of the truck. (No units required)"))
            if answer == 20:
                score += 1
            elif answer >= 0 and answer < 20:
                score -= 1 
            elif answer > 20:
                score -= 1
print(score)
time.sleep(1)

#fix elif statement
print("\nQuestion Seven - Friction")
num_questions += 1

print("\nThere are four forces that make up the basic net force.")

answer = input("\nWhat is the name of the force that opposes motion(thrust force)?").strip().lower()

if answer == "drag" or answer == "friction":
    score += 1
elif "0" in answer or "1" in answer or "2" in answer or "3" in answer or "4" in answer or "5" in answer or "6" in answer or "7" in answer or "8" in answer or "9":
    print("\nThis is a word based answer. Just how did a number end up in your answer?\n"
    "I'll give you one more chance to complete this question.")
    answer = input("\nWhat is the name of the force that opposes motion(thrust force)?").strip().lower()
    if answer == "drag" or answer == "friction":
        score += 1
    else:
        score -= 1
else:
    score -= 1
    
print(score)
time.sleep(1)

print("\nQuestion Eight - Velocity in acceleration")
num_questions += 1

answer = input("\nIn acceleration = v/t, do you find v by:\n"
"A. Multiplying acceleration by time\n"
"B. Dividing acceleration by time\n"
"C. None of the above").strip().lower()

if answer == "a":
    score += 1
elif answer == "b" or answer == "c":
    score -= 1
else:
    while answer != "a" and answer != "b" and answer != "c":
        print("\nNote: The only options are: A, B, or C. Select one of the available options.")
        answer = input("Which is the correct answer?").strip().lower()
        if answer == "a":
            score += 1
        elif answer == "b" or answer == "c":
            score -= 1

print(score)
time.sleep(1)

print("\nQuestion Nine - Acceleration-time graph")
num_questions += 1

print("\nWhen looking at an acceleration-time graph, how do you calculate the total distance of a line that slopes upwards(triangle)?")

answer = input("A. b*h\n"
"B. ½b*h\n"
"C. πr^2\n"
"D. None of the above").strip().lower()

if answer == "a" or answer == "c" or answer == "d":
    score -= 1
elif answer == "b":
    score += 1
else:
    while answer != "a" and answer != "b" and answer != "c" and answer != "d":
        print("\nNote: Select one of the given options.")
        answer = input("Which is the correct answer?").strip().lower()
        if answer == "a" or answer == "c" or answer == "d":
            score -= 1
        elif answer == "b":
            score += 1

print(score)
time.sleep(1)

#Won't display negative scores
if score <= 0:
    score -= score
    
print("\nYou got {1}/{0} correct".format(num_questions, score))

if score >= 0 and score <= 2:
    print("\nYou got {1}/{0} correct. Looks like you might want to improve your physics skills a bit, huh?".format(num_questions, score))
if score > 2 and score <= 4:
    print("\nYou got {1}/{0} correct. You could do better.. Practice a little, would ya?".format(num_questions, score))
if score >4 and score <= 6:
    print("\nYou got {1}/{0} correct. Not too bad. There's still room for improvement though.".format(num_questions, score))
if score >6 and score <= 10:
    print("\nYou got {1}/{0} correct. Wow, look at you! You're pretty good, huh? Great job.".format(num_questions, score))
    
time.sleep(3)

print("\nYou have reached the ending of Patrick Pancho Setu's AS91883 Python Quiz.")
time.sleep(3)

print("\nCongratulations upon your completion of the quiz!")







