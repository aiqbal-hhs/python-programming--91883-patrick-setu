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
#SYNC = orange text
#stdout = blue text
#hit = white text, black background
#ERROR = black text, red background
#sel = black text, grey Background

#
#Orange score at the end
#Red for warnings
#Green for 'true' and red for 'false' in questions
#Green for useful information
#Purple for questions text
#Blue for input


score = 0
num_questions = 0

colour.write("Welcome to ","SYNC")
colour.write("Patrick Pancho Setu's","ERROR")
colour.write(" AS91883 Python Quiz! \n","SYNC")

colour.write("\nEach question is worth a point. Try and earn as many points as possible. The total points earned will be displayed at the end of the quiz. \n","SYNC")
#set to 10s
#Allows the user to have enough time to read the text without immediately starting the quiz
time.sleep(0.1)

colour.write("\nSome formulas that may be of use: \n"
    "velocity = d/t | acceleration = v/t | Force = ma | Power = W/t | Work = Fd\n","STRING")
time.sleep(3)

colour.write("\nTip: You may refer to the formulas provided while answering the questions. \n","STRING")
time.sleep(3)

#3 second timer indicating time til start of quiz
colour.write("\nThe quiz will begin in:","SYNC")
time.sleep(1)

colour.write("\n3..","COMMENT")
time.sleep(1)

colour.write("\n2..","KEYWORD")
time.sleep(1)

colour.write("\n1..\n","STRING")
time.sleep(1)

colour.write("\nThe quiz will now begin.\n","SYNC")
time.sleep(1)

#Question One code
colour.write("\nQuestion One - Gravity","BUILTIN")
num_questions += 1

colour.write("\nThe acceleration of gravity is 10ms-1 for Level 1 mechanics.","SYNC")

colour.write("\nTrue","STRING")
colour.write(" or ","SYNC")
colour.write("False\n","COMMENT")

answer = input().strip().lower()

if answer == "true":
    score += 1
else:
    while answer != "true" and answer != "false":
        colour.write("\nNote: Enter an appropriate answer. \n","COMMENT")
        colour.write("\nTrue","STRING")
        colour.write(" or ","SYNC")
        colour.write("False\n","COMMENT")
        answer = input().strip().lower()
        if answer == "true":
            score += 1

print("\n{} points".format(score))
time.sleep(0.5)

#Question Two code
colour.write("\nQuestion Two - Work","BUILTIN")
num_questions += 1

colour.write("\nA box filled with heavy materials has a weight of 1500N. A forklift lifts the box upwards 2 metres. The forklift takes 10 seconds to lift the box. ","SYNC")

#fix decimal problem caused by float
answer1 = int(input("\nCalculate the work done. (No units required)\n"))

if answer1 == 3000:
    score += 1
elif answer1 >= 10000:
    colour.write("\nWoah there buddy. You're a bit too far off. \n"
    "Try again. \n","COMMENT")
    answer1 = int(input("\nCalculate the work done. (No units required)\n"))
    if answer1 == 3000:
        score += 1
    elif answer1 <= 0:
        if answer <= 0:
            colour.write("\nHmm. That isn't possible. \n"
            "I'll give you another chance. \n","COMMENT")
            answer1 = int(input("\nCalculate the work done. (No units required)\n"))
            if answer1 == 3000:
                score += 1

print("\n{} points".format(score))    
time.sleep(0.5)

#might need fixing
if answer1 == 3000:
    answer1 += 4500
if answer != 3000:
    amswer1 = answer1*0+7500

#Question Three code
colour.write("\nQuestion Three - Power","BUILTIN")
num_questions += 1
#fix
print("\nUsing the answer from the previous question, what is the amount of power required to lift the box if it takes 10 seconds? \n"
    "A. {:.0f}W \n"
    "B. 450W \n"
    "C. 300W".format(answer1/10))
    
answer = input("\nIs the answer: A, B, or C?\n").strip().lower()

if answer == "c":
    score += 1
else:
    colour.write("\nNote: The only options are: A, B, or C. Select one of the available options.\n","COMMENT")
    while answer != "a" and answer != "b" and answer != "c":
        answer = input("\nIs the answer: A, B, or C?\n").strip().lower()
        if answer == "c":
            score += 1

print("\n{} points".format(score))
time.sleep(0.5)

#Question Four code
colour.write("\nQuestion Four - No work done","BUILTIN")
num_questions += 1

colour.write("\nThe forklift from Question 2 has now finished lifting the box upwards and now remains motionless.","SYNC")

answer = input("\nIs there being work done after the 1500N box has been lifted for 10 seconds?\n").strip().lower()
if answer == "no":
    score += 1
else:
    while answer != "yes" and answer != "no":
        colour.write("\nNote: This is a yes or no question. Please answer as such.\n","COMMENT")
        answer = input("\nIs there being work done after the 1500N box has been lifted for 10 seconds?").strip().lower()
        if answer == "no":
            score += 1

print("\n{} points".format(score))
time.sleep(0.5)

#Question Five code
colour.write("\nQuestion Five - Mass and weight","BUILTIN")
num_questions += 1

colour.write("\nIn science, the mass of an object and the weight of an object are the same thing.","SYNC")

colour.write("\nTrue","STRING")
colour.write(" or ","SYNC")
colour.write("False\n","COMMENT")

answer = input().strip().lower()

if answer == "false":
    score += 1
else:
    while answer != "true" and answer != "false":
        colour.write("\nNote: Enter an appropriate answer. \n","COMMENT")
        colour.write("\nTrue","STRING")
        colour.write(" or ","SYNC")
        colour.write("False\n","COMMENT")
        answer = input().strip().lower()
        if answer == "false":
            score += 1

print("\n{} points".format(score))
time.sleep(1)


#fix float problem here as well
#Question Six code
colour.write("\nQuestion Six - Speed","BUILTIN")
num_questions += 1

colour.write("\nA truck is driving along the motorway. It travels 100 metres in the span of 5 seconds.","SYNC")

answer = int(input("\nCalculate the speed of the truck. (No units required)\n"))

if answer == 20:
    score += 1
elif answer < 0:
    colour.write("\nNot quite possible. Speed can't be negative.\n"
    "Try again.\n","COMMENT")
    while answer < 0:
        answer = int(input("\nCalculate the speed of the truck. (No units required)\n"))
        if answer == 20:
            score += 1
        elif answer > 0:
            score += 0
        else:
            colour.write("\nNot quite possible. \n"
            "You have got one more chance.\n","COMMENT")
            answer = int(input("\nCalculate the speed of the truck. (No units required)\n"))
            if answer == 20:
                score += 1

print("\n{} points".format(score))
time.sleep(1)

#fix elif statement(numbers)
#Question Seven code
colour.write("\nQuestion Seven - Friction","BUILTIN")
num_questions += 1

colour.write("\nThere are four forces that make up the basic net force.","SYNC")

answer = input("\nWhat is the name of the force that opposes motion(thrust force)?\n").strip().lower()

if answer == "drag" or answer == "friction":
    score += 1
elif "0" in answer or "1" in answer or "2" in answer or "3" in answer or "4" in answer or "5" in answer or "6" in answer or "7" in answer or "8" in answer or "9":
    colour.write("\nThis is a word based answer. Just how did a number end up in your answer?\n"
    "I'll give you one more chance to complete this question.","COMMENT")
    answer = input("\nWhat is the name of the force that opposes motion(thrust force)?\n").strip().lower()
    if answer == "drag" or answer == "friction":
        score += 1
    
print("\n{} points".format(score))
time.sleep(1)

#Question Eight code
colour.write("\nQuestion Eight - Velocity in acceleration","BUILTIN")
num_questions += 1

colour.write("\nIn acceleration = v/t, do you find v by:\n","SYNC")

answer = input("A. Multiplying acceleration by time\n"
"B. Dividing acceleration by time\n"
"C. None of the above\n").strip().lower()

if answer == "a":
    score += 1
else:
    while answer != "a" and answer != "b" and answer != "c":
        colour.write("\nNote: The only options are: A, B, or C. Select one of the available options.\n","COMMENT")
        answer = input("\nWhich is the correct answer?\n").strip().lower()
        if answer == "a":
            score += 1
            
print("\n{} points".format(score))
time.sleep(1)

#Question Nine code
colour.write("\nQuestion Nine - Acceleration-time graph","BUILTIN")
num_questions += 1

colour.write("\nWhen looking at an acceleration-time graph, how do you calculate the total distance of a line that slopes upwards(triangle)?","SYNC")

answer = input("\nA. b*h\n"
"B. ½b*h\n"
"C. πr^2\n"
"D. None of the above\n").strip().lower()

if answer == "b":
    score += 1
else:
    while answer != "a" and answer != "b" and answer != "c" and answer != "d":
        colour.write("\nNote: Select one of the given options.\n")
        answer = input("Which is the correct answer?\n").strip().lower()
        if answer == "b":
            score += 1

print("\n{} points".format(score))
time.sleep(1)

#Question Ten code

#make score colour orange    
colour.write("\nYou got {1}/{0} correct".format(num_questions, score))

if score >= 0 and score <= 2:
    colour.write("\nYou got {1}/{0} correct. Looks like you might want to improve your physics skills a bit, huh?".format(num_questions, score))
if score > 2 and score <= 4:
    colour.write("\nYou got {1}/{0} correct. You could do better.. Practice a little, would ya?".format(num_questions, score))
if score >4 and score <= 6:
    colour.write("\nYou got {1}/{0} correct. Not too bad. There's still room for improvement though.".format(num_questions, score))
if score >6 and score <= 10:
    colour.write("\nYou got {1}/{0} correct. Wow, look at you! You're pretty good, huh? Great job.".format(num_questions, score))
    
time.sleep(3)

colour.write("\nYou have reached the ending of Patrick Pancho Setu's AS91883 Python Quiz.\n")
time.sleep(3)

#change display colour
colour.write("\nCongratulations upon your completion of the quiz!")







