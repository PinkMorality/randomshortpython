from random import *

damageskills = ["onehand/twohand", "block", "archery", "destruction"]
armorskills = ["light armor", "heavy armor", "alteration"]
supportskills = ["illusion", , "pickpock", "restoration", "conjuration"] #can use sneak depending on build
#enchanting and smithing go to 100 from cheats, alchemy and speech used every run,
#lockpick also used ##but if chosen, means have to invest perks
while True:
    archoice = [armorskills[randint(0,2)]]

    d2s2choice = randint(0,1)

    if d2s2choice == 1:
        dchoice = sample(damageskills, k=2)
        schoice = sample(supportskills, k=3)
    else:
        dchoice = sample(damageskills, k=3)
        schoice = sample(supportskills, k=2)

    final = [archoice + schoice + dchoice]


    input(final)
