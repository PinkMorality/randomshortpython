from random import *

damageskills = ["onehand", "block", "twohand", "archery", "destruction", "conjuration"]
armorskills = ["light armor", "heavy armor", "alteration"]
supportskills = ["illusion", "sneak", "lockpick", "pickpock", "speech", "restoration"]
#enchanting and smithing go to 100 from cheats, alchemy used in every run for money
while True:
    archoice = [armorskills[randint(0,2)]]

    d2s2choice = randint(0,1) #1 = 3 damage,0 = 2 damage

    if d2s2choice == 0:
        dchoice = sample(damageskills, k=2)
        schoice = sample(supportskills, k=3)
    else:
        dchoice = sample(damageskills, k=3)
        schoice = sample(supportskills, k=2)

    final = [archoice + schoice + dchoice]


    input(final)