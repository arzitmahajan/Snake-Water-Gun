import random
def game(comp,u):
    if comp == 's':
        if u == 'w':
            return False
        elif u == 'g':
            return True
        elif comp == u:
            return None
    if comp == 'w':
        if u == 's':
            return True
        elif u == 'g':
            return False
        elif comp == u:
            return None
    if comp == 'g':
        if u == 's':
            return False
        elif u == 'w':
            return True
        elif comp == u:
            return None


print("computer's Turn :snakes(s) water(w) or gun(g) ?",)
rand = random.randint(1,3)
if rand == 1:
    comp = 's'
elif rand == 2:
    comp = 'w'
elif rand == 3:
    comp = 'g'

u = input(" Your's Turn :snakes(s) water(w) or gun(g) ?")
a = game(comp,u)

print(f"computer chose {comp}")
print(f"you chose {u}")

if a == None:
    print("the game is tie")
elif a :
    print("YOU WON!")
else :
    print("YOU LOSE!")

game(comp,u)