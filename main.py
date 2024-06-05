#greet the user and introduce the quiz
import random

x = random.randint(1,100)
y = 2*x**3 + 4*x**2 + 12/x + 2
print(y)
play = input("Do you want to play?").lower()
while play == "yes":
    print("ok")
    score = 10
    QUESTION_FORMAT = "{}\nA.{} B.{} C.{} D.{}"
    SHANXI_LIST = ["Jingyang Lake","Longtan Park","Yingze Pak"]
    OK_COMMENTS = ["It's not bad.","It's good.","Correct!"]
    NOOK_COMMENTS = ["It's not good.","It's bad.","Wrong!","You are sb."]
    print("Hello!")
    name = input("What is your name?")
    while True:
        if name == "":
            print("Please write your name")
            name = input("What is your name?????")
        else:
            break
    print("Welcome to the quiz!", name)
    score = 10
    play = "yes"

#Ask the user a question
    answer = input("Where is the capital of China?").upper()
    answer1 = input("How many provinces are there in China?")

#Tell them the correct answer
    if answer == "Beijing".upper():
        print(random.choice(OK_COMMENTS))
        score += 10
    elif answer == "":
        print("write something")
        score -= 10
    else :
        print("Beijing is truth")
        score -= 10
    if int(answer1) == 34:
        print(random.choice(OK_COMMENTS))
        score += 10
    elif int(answer1) <34 :
        print("There are more provinces")
    elif int(answer1) >34 :
        print("There are less provinces")
    question = "Where is the capital of Shanxi?"
    a = "Taiyuan"
    b = "Linfen"
    c = "Changzhi"
    d = "Jincheng"
    answer2 = input(QUESTION_FORMAT.format(question, a, b, c, d)).lower()
    if answer2 == "a" or answer2 == a:
        print(random.choice(OK_COMMENTS))
        score += 10
    elif answer2 != "a" and answer2 != a and answer2 != "b" and answer2 != b and answer2 != "c" and answer2 != c and answer2 != "d" and answer2 != d:
        print("Taiyuan is truth,",random.choice(NOOK_COMMENTS))
    else:
        print("Taiyuan is truth") 
    answer3 = input("Do you want to go to Taiyuan?").lower()
    if answer3 == "yes" or answer3 == "yeah":
        print("哟西")
        score += 10
        while answer3 == "no":
            print(random.choice(NOOK_COMMENTS))
            answer3 = input("Do you want to go to Taiyuan?").lower()
#End the quiz
    if score == 0:
        print("You have no points.",random.choice(OK_COMMENTS))
    else:
        print(OK_COMMENTS[1],"Your score is", score)
        print("Thank you for playing!{}", format(name))
    play = input("Do you want to play again?").lower()
