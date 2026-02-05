import random 

def game():
    print("Game is starting")

    with open("hi_score.txt","r") as f:
        hi_score = f.read()
        if(hi_score != ""):
            hi_score = int(hi_score)
        else:
            hi_score = 0

    score = random.randint(1,100)
    if(score > hi_score):  
        print(f"Congratulations! You set a new high score: {score}")
        with open("hi_score.txt","w") as f:
            f.write(str(score))
    else: 
        print(f"Your score is {score}")

game()