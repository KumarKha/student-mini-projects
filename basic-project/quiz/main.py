
score = 0


question = input("Q1: How many players are on the field for each team in a standard soccer match? ")
if int(question) == 11:
    score += 1
    print("Correct")
else:
    print("Wrong")
question = input("Q2: A touchdown in American football is worth 6 points. true or false? ")
if question == "true":
    score += 1
    print("Correct")
else:
    print("Wrong")
question = input("Q3: What sport is known as “the beautiful game”? ")
if question == "soccer":
    score += 1
    print("Correct")

print("You scored:",score)