
def whatbedis():
    print("As a member of the community you rise through the ranks and eventaully run for president in the Libertarian Party.")
    print("The End.")

def finale():
    print("While enjoying your party to celebrate you joining the community, you over hear an old man saying his wife has diverticulitis and that his dog is as stupid as his son.")
    answer = input("Do you believe the story? ").lower()
    if answer == "yes":
        print("He turned out to be a WWII veteran and the story was a hilarious summary of his life.")
        print("The town loves you even more for respecting and having fun with the elderly which made up 60% of Winfield's population.")
        whatbedis()
    elif answer == "no":
        print("The town sees that you are disrespectful of you elders which make up 60% of the Winfield population. Your welcoming party has now become a never come back party. You were this close man come on!")
        part1()
    else:
        print("Please enter a vaild answer")
        finale()

def part13():
    print("On your way back from the devil's lettuce incident you find a 'neat' looking flashlight.")
    answer = input("Do you bring the flashlight with you and pretend it is a gun to look cool? ").lower()
    if answer == "yes":
        print("The police are called because someone thinks it is a real gun and you are arrested for causing such a confusion.")
        print("You die in jail for your crimes against relaxation.")
        part1()
    elif answer == "no":
        print("You passed the tests of the community and are offically announced a member of Winfield.")
        finale()
    else:
        print("Please enter a vaild answer")
        part13()

def part12():
    print("You come across some of the devil's lettuce and rum. Your friends are good libertarians and want nothing to do with it.")
    answer = input("Do you partake of the devil's lettuce and bring the rum too? ").lower()
    if answer == "yes":
        print("You do not know da way of the Libertarians. Everyone thinks you are an alcoholic and are trying to drown your sorrows. You are rejected from the community and left for dead. THIS IS WINFIELD!")
        part1()
    elif answer == "no":
        print("You passed the test and are permitted to continue living in the community.")
        part13()
    else:
        print("Please enter a vaild answer")
        part12()

def part11():
    print("Your party travels back to the General Store to play a game of Yu-gi-oh and eat.")
    print("Before playing, Pan asks you which deck you would like to play as.")
    answer = input("Do you choose zombies, harpies, or jinzo? ").lower()
    if answer == "zombies":
        print("You activated his trap card and he summoned Blue Eyes White Dragon.")
        part12()
    elif answer == "harpies":
        print("You managed to win but it was tough and now your exhausted.")
        part12()
    elif answer == "jinzo":
        print("You won by a landslide and destroyed him at every turn.")
        part12()
    else:
        print("Please enter a vaild answer")
        part11()

def part10():
    print("You return to the home of Pan Darrillo and stay to endure his mother's famously awful cooking.")
    answer = input("You are offerred a meatball, do you take it? ").lower()
    if answer == "yes":
        print("You try to consume it but end up throwing it back up behind a stump in their yard.")
        part11()
    elif answer == "no":
        print("You made a smart decision because the meatballs were inedible.")
        part11()
    else:
        print("Please enter a vaild answer")
        part10()


def part9():
    print("After nearly losing your life you continue on through the strange town to explore its other oddities.")
    print("Along your journey you encounter 2 boys by the names of Pan Darrillo and Waise Blilson. You befriend the 2 and they accompany you on your journey through WInfield.")
    print("The 3 of you go back to the bball courts and join the other teens in a quick game.")
    print("While splitting into teams you find a swivel chair that is crumbling apart.")
    answer = input("Do you continue playing bball with the bois? ").lower()
    if answer == "yes":
        print("Your team loses cause you have never played bball before in your life. Somehow you managed to break a fish tank 30 feet away.")
        part10()
    elif answer == "no":
        print("You spin around in the swivel chair while the bois play around you. You get so dizzy and dehydrated you puke.")
        part10()
    else:
        print("Please enter a vaild answer")
        part9()

def part8():
        global answer
        print("After walking outside, you see some fellow youth playing some bball outside the school, when a couple of guys, they were up to no good, started causing trouble in the neighborhood.")
        print("You walk over to the courts and confront the thugs.")
        print("The hoodlems pull knives out and threaten to come at you.")
        answer = input("Do you continue to approach the gangstas and risk your life? ").lower()
        if answer == "yes":
            print("The first attacker approaches you and slashes towards your neck.")
            print("You have died. Shouldve bought some items from the store or not tried to be a hero.")
            part1()
        elif answer == "no":
            print("You run away and leave the bois to die. You hear the bois screaming eachothers' names in agony while being beaten.")
            part9()
        else:
            print("Please enter a vaild answer")
            part8()

def part7():
        global player_inventory
        print("After walking outside, you see some fellow youth playing some bball outside the school, when a couple of guys, they were up to no good, started causing trouble in the neighborhood.")
        print("You walk over to the courts and confront the thugs.")
        print("The hoodlems pull knives out and threaten to come at you.")
        answer = input("Do you continue to approach the gangstas and risk your life? ").lower()
        if answer == "yes":
            print("You pull out a ham sandwich and find that the deli workers forgot their butcher knife in your sandwich.")
            print("You throw the knife at the bigger of the 2 attackers and it strikes him in the leg.")
            print("Congratulations, you've mortally wounded a stranger. The two men limp and run away in fear of what else you might have.")
            if 'key' in player_inventory:
                del player_inventory['ham sandwich']
            part9()
        elif answer == "no":
            print("You run away and leave the bois to die. You hear the bois screaming eachothers' names in agony while being beaten.")
            part9()
        else:
            print("Please enter a vaild answer")
            part7()

def part6():
        global player_inventory
        print("You begin walking into Winfield and find that it is rather small. The center of attention for its residents is the General Store.")
        print("You make your way to the store and see that the workers are very lazy and unwilling to work. You spot the store's owner and decide to talk to her.")
        print('You ask her "What is this place and why does everyone in town come here?"')
        print('She replies, "The store is a bakery,a deli, a general store, and a pharmacy. Here is some money. The store needs more business so please buy something."')
        answer = input("Do you take her money and buy something? ").lower()
        if answer == "yes":
            print("The owner says that her name is Sandy and that she is glad people like you are in the community.")
            print("After your conversation with Sandy you realize she is missing a few screws but has sweet intentions for her town.")
            print("You now make your way around the store looking for items that might benefit you.")
            print("You grab a bottle of Tylenol, a soda, some bleach, and have a ham sandwich made for you.")
            print("You leave the store.")
            player_inventory = {'tylenol': 1,'soda': 1,'bleach': 1,'ham sandwich': 1}
            part7()
        elif answer == "no":
            print("The owner is disappointed in your choice and sees you as a detriment. You leave the store.")
            part8()
        else:
            print("Please enter a vaild answer")
            part6()

def part5():
        print("Welcome to the Township of Winfield. We hope you enjoy your time here. Be sure to be a responsible member of society (unlike libertarians) and contribute to the benefit of the community.")
        part6()

def part4():
        answer = input("Are you an American citizen? ").lower()
        if answer == "yes":
            part5()
        elif answer == "no":
            print("You failed to be accepted into Winfield. Try again.")
            part1()
        else:
            print("Please enter a vaild answer")
            part4()

def part3():
        answer = input("Are you of the white ethnicity? ").lower()
        if answer == "yes":
            part4()
        elif answer == "no":
            print("You failed to be accepted into Winfield. Try again.")
            part1()
        else:
            print("Please enter a vaild answer")
            part3()

def part2():
        answer = input("Do you have family currently living in Winfield? ").lower()
        if answer == "yes":
            part3()
        elif answer == "no":
            print("You failed to be accepted into Winfield. Try again.")
            part1()
        else:
            print("Please enter a vaild answer")
            part2()

def part1():
    print("Welcome to the town of Winfield")
    answer = input("Are you looking to move to Winfield? ").lower()
    if answer == "yes":
        part2()
    elif answer == "no":
        print("You failed to be accepted into Winfield. Try again.")
        part1()
    else:
        print("Please enter a vaild answer")
        part1()

def intro():
    print("You are entering the town of Winfield.")
    name = input("what is your name traveller: ").lower()
    if name == "gary johnson":
        print("You are Winfield's God. You win.")
        whatbedis()
    elif name == "ron paul":
        print("You are Winfield's God. You win.")
        whatbedis()
    elif name == "adam kokesh":
        print("Please enter a name that does not belong to a psychopath.")
        intro()
    else:
        print(f"Hi {name}")
        part1()

intro()
