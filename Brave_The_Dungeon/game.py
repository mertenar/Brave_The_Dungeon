
import sys
import random
import time

#global settings. 3 lives and 200 gold is standard
lives = 3
global gold
gold = 200
global character_name
character_name = ""


def text_delay(text):
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.05)


#character class allows for the user to create own name that is referenced throughout
class Character(object):

    def make_character_name(self):
        character_name = raw_input("\nWhat will you name your noble prince... er peasant?  ")
        global character_name
        self.greeting = "Best of luck to you brave %s." % (character_name)
        print self.greeting


#Parent class scene was created with 'enter' function, though each child class overrides 'enter' anyhow.
#This could give the potential for all rooms to inherit something easily
class Scene(object):

    def enter(self):
        print "You pull yourself into the next room and are anxious to see what awaits."
        scene.enter()


#This was initially set up when the Player had 1 life, improved with the life system
class Death(Scene):

    def enter(self):
        print "Dead"
        sys.exit()


#first scene that's run in the game, calls instance of character class to create name
#background story is set up and The Player learns basic outline of the game
class Intro(Scene):

    def enter(self):

        print "\n", "*" * 50, "\nWelcome to Brave the Dungeon. Hope you brought your cohones!"
        raw_input("\nPress ENTER if you found them and let's get started...")
        text = """\nThe snow falls lightly upon your brow as you trudge through the snow,
each step bringing you closer to the large wooden door at the base of the tower.
This had felt more like a dream before. One that you just can't seem to shake in your sleep.
Yet, now grasping the large brass knob, this couldn't feel more real.
You're here seeking the prize of the local legend. One of those sorts involving a princess
and a hulking prince to save her. Though you\'re a lame ass peasant boy and will need a miracle...\n"""
        text_delay(text)

        playcharacter.make_character_name()

        raw_input("\nPress ENTER to turn the knob." )

        text = """\nIt takes two hands to twist the frozen knob and push the door open.
Awaiting you is a ramp into pitch black. To the right of the door you notice a sign reading -
\"%s, access the black market by stomping your foot three times!\" Okay... Wait they knew my name? Anyway...
You sling your backpack over your shoulder and prepare yourself for the task ahead.""" % (character_name)
        text_delay(text)

        raw_input("\n\nPress ENTER to... do just that and start your journey." )

        playthrough.player_move('gnomes')


#First challenge room where player can lose life. This challenge is a riddle
class GnomeRoom(Scene):

    def enter(self):

        text = """\nYour first step doesn't connect with solid ground. You end up sliding down a steep ramp.
You continue to pick up speed down the ramp when you suddenly reach the bottom with a bone-jarring thud.
All around you is so much activity - flutes are playing, large mugs being clanged together as odd looking
folk shout and laugh around large, wooden tables. You seem to be in the center of a quite
jolly gnome bar.
"""
        text_delay(text)

        raw_input("\nPress ENTER to gather yourself after that fall." )

        text = """\nAs you catch your breath and look around one gnome recognizes your presence.
He quickly puts down his glass and sprints over. \"Hiya there sir!\"
\"Guess you're here to play the game!\" he exclaims as he whips out a short sword and aims it towards
your stomach. \"You must answer the following question or feel this up your gut!\"
\"What comes in three major colors, will eat man and berries alike, and sleeps through Santa's coming?\"
"""
        text_delay(text)

        answer = raw_input("\nYou eye the sharp blade of the sword and carefully respond with: " )

        if 'bear' in answer or 'Bear' in answer:
            text = "\"Right on! You may proceed through the door at the end of the hall when ready.\""
            text_delay(text)
            playthrough.player_move('race_betting')

        else:
            game_life.lose_life()
            playthrough.player_move('gnomes')


#challenge here is making a guess at a race outcome
#player can purchase item to make the challenge way easier
class RacebettingRoom(Scene):

    def enter(self):

        text = """\nYou open the door to the next room. In the middle of the room is a giant track.
Around the track there are stands full of all kinds of creatures. They shout at
3 creatures in the middle running around the track. It seems that they are betting on this peculiar race.
You then notice a stack of betting cards in front of you.
You also notice that the door on the other side of the room with \"200 gold required\" printed above it.
        """
        text_delay(text)

        raw_input("\nPress ENTER to take a betting card and have a seat.")

        text = """\nYou take a seat and study the card. There are 3 choices on the card.
1) Centaur
2) Basilisk
3) Three-headed dog
The bookie comes and demands a choice!
        """
        text_delay(text)

        if "race guide" in player_inventory.pack_items:
            text = """You quickly peek at the race guide you bought. It's writing from the merchant that reads,
\"After observations on many races... the Centaur will almost always win, unless the basilisk wraps him up.\"
"""
            text_delay(text)
        else:
            text = """
You nervously study the options on the card...
"""
            text_delay(text)

        self.race()

    def race(self):
        race_choice = raw_input("\n\nWhich racer do you choose? (1. Centaur, 2. Basilisk, 3. Three-headed dog) --> ")
        if '1' in race_choice or 'centaur' in race_choice or 'Centaur' in race_choice:
            choice = "Centaur"
        elif '2' in race_choice or 'basilisk' in race_choice or 'Basilisk' in race_choice:
            choice = "Basilisk"
        elif '3' in race_choice or 'Three-headed dog' in race_choice or 'three-headed dog' in race_choice:
            choice = "Three-headed dog"
        else:
            print "That choice isn't on the card, please try picking again."
            self.race()
        global gold
        bet_amount = raw_input("How much do you wager? You have %d gold. --> "% gold)
        bet_amount = int(bet_amount)
        if bet_amount <= gold:
            pass
        else:
            print "You don't have that much gold! Try again!"
            self.race()

        raw_input("You have put %s on %s. Good luck! Press ENTER to start the race." % (bet_amount, choice))
        winning_number = (random.randint(1,10))

        if winning_number < 9:
            winner = "Centaur"
            text = """\nThe cannon blasts and the race is on! The centaur takes off with tremendous speed.
The others don't even stand a chance as the centaur finishes each lap in just mere seconds.
            """
            text_delay(text)
        if winning_number >= 9:
            winner = "Three-headed dog"
            text = """\nThe centaur leaps to attempt an early lead but is quickly grabbed by the basilisk.
The basilisk just wraps it up and sits there as the centaur pouts.
The dog slowly but surely bounds its way around the track to an easy win.
            """
            text_delay(text)

        if winner == choice:
            gold = gold + bet_amount
            print "You win! You won %d and now have %d." % (bet_amount, gold)
        else:
            text = """\nLooks like you aren't too good at this.
You begrudgingly pay the bookie..."""
            text_delay(text)
            gold = gold - bet_amount

        if gold <= 0:
            self.soul_reaper()

        else:
            pass

        choice = raw_input("\nDo you stay for another race or head out? --> ")
        if "stay" in choice or "again" in choice or "race" in choice:
            print "You study the racers and think about your next bet."
            self.race()
        else:
            self.leave_room()


    def leave_room(self):
        text = """You approach the door at the other end of the race track. Above the door reads \"200 gold\".
A slot next to the door says \"Insert gold here for entry\" Put in the gold?
*You will get to visit the merchant after if you choose to.
"""
        text_delay(text)

        global gold
        if gold >= 200:
            choice = raw_input("--> ")
            if choice == "yes" or choice == "Yes":
                text = """You insert the gold and the door slides open. You cautiously enter.
Your gold is actually given back... A voice echoes \"You will need this later...\"
                """
                text_delay(text)
                playthrough.player_move('darkpool')
            elif choice == "No" or choice == "no":
                self.race()
            else:
                print "Try yes or no..."
                self.leave_room()
        else:
            print "You don't have enough gold! Go win some more!"
            self.race()


#had to implement some way to use a life to convert to gold instead of just losing
    def soul_reaper(self):
        text = """\n\nLooks like you are out of gold... that's not going to get you far. You see a dark hooded creature
behind a booth in the corner. The top of the booth reads \"I pay you 100 gold to let me eat your soul\".
            """
        text_delay(text)

        choice = raw_input("\nHave your soul eaten %s? --> " % character_name)
        if "yes" in choice or "Yes" in choice:
            text = """You asked for it... The creature swiftly tilts your head back and
sucks out your soul via a horrifying french kiss.
"""
            text_delay(text)
            game_life.lose_life()
            global gold
            gold = gold + 100
            print "You now have %d gold." % gold
        elif "no" in choice or "No" in choice or "over" in choice or "Over" in choice:
            print "Based on your stupid choice..."
            game_life.game_over()
        else:
            print "I didn't get that... try picking again."
            self.soul_reaper()


#challenge here is to have the mandatory item in inventory to clear the room
class DarkpoolRoom(Scene):

    def enter(self):

        text = """\nYou enter the next room. This room is small in comparison to the previous. Also it's very dim.
It appears as if you are on the side of a well. There is a ledge you stand on,
then below is a large pit with the sound of rushing water, and another ledge with a door
on the other side with \"PRINCESS:):)\" printed above it in shiny gold lettering.
"""
        text_delay(text)
        raw_input('Press ENTER to think of a way to get to the other side...')
        text = """You ponder any possible way across. You look up, and you catch the glimmer of something metal.
It almost looks like a hook. If you only had some rope that you could attach to it and swing across.
     """
        text_delay(text)
        self.cross()

    def cross(self):

        if "rope" in player_inventory.pack_items:
            print "\nYou have a rope!"
            text = """You swing the rope around just like you would back at the farm.
You throw the lasso hard up onto the hook. It tightens right on. Maybe a
peasant does have some useful skills for this.
You swing yourself across the dark pond and land on the other side.
None of that dramatic arm waving shit as you barely land it. You got it solid.
You are ready for your prize.... You open the door labeled \"PRINCESS:):)\" to get what's yours.
            """
            text_delay(text)
            player_inventory.pack_items.remove("rope")
            playthrough.player_move('false_princess')

        else:
            print "Looks like you don't have a rope. There's no other way so you need to go back to the merchant."
            playdungeon.scenes['merchant'].enter()
            self.cross()


#challenge here should be an easy choice, this is more for just comedic value
class FalseprincessRoom(Scene):

    def enter(self):

        text = """\nAs you enter the room you puff up your chest and act like as much of a man
as you can muster. You see a beautiful, white four post bed with candles sorrounding it.
In the middle of the bed you see the princess facing the other way sleeping in an elegant pink
dress. You pick up the pace towards the bed as the scent of an interesting perfume reaches you.
Also you notice a small plaque next to the bed that reads,
    \"Roses must be placed on the bed prior to *entry*.\"
 """
        text_delay(text)
        self.seduction_time()

    def seduction_time(self):

        if "roses" in player_inventory.pack_items:
            print "\nYou have the roses in your inventory."
            raw_input("\nPress ENTER to claim your prize.")
            self.getlaid()

        else:
            text = """\nLooks like you need the roses to finish this...
you step outside quickly to talk to the merchant to get some.
 """
            text_delay(text)
            playdungeon.scenes['merchant'].enter()
            self.seduction_time()

    def getlaid(self):
        text = """\nYou approach the bed, laying the roses down in front of you.
Just as you jump into the bed the perfume hits your nose stronger than ever.
\"Come to me baby\", you hear in a voice about 5 octaves lower than you were expecting.
Also, that's not perfume. It almost smells like troll shit. The princess turns towards you uttering a
deep growl. You quickly spot the pointed nose and pimply, puss ridden troll face... winking at you.
"""
        text_delay(text)

        choice = raw_input("\nStay and get cozy with the troll in the dress or GET THE FUCK OUT? --> ")
        if 'stay' in choice or 'Stay' in choice or 'cozy' in choice or 'Cozy' in choice:
            text = """\nYou snuggle right up to that troll and nothing comes between you and
what you are going to claim as a glorious *finish*. Pow pow. Not how you thought you
would lose your V card but whatever, better than an animal back at the farm I guess.
"""
            text_delay(text)
            player_inventory.pack_items.remove("roses")
            game_life.lose_life()

        elif 'leave' in choice or 'out' in choice or 'run' in choice or 'flee' in choice:
            print
            text = """You NOPE the fuck right out of there, not even looking back for a second.
You sprint to the other end of the room and fling open the door leading to the next room.
"""
            text_delay(text)
            playthrough.player_move('dragon')

        else:
            print "\nDidn't understand that, please pick again."
            self.getlaid()


#the last test before victory. challenge requires multiple items and multiple correct choices
class DragonRoom(Scene):

    def enter(self):
        text = """\nGlad to be out of that last situation, you cautiously move forward.
Definitely need to be more careful. Moving through a tunnel, there doesn't seem
to be an end for a bit. Up ahead you see a sign that reads, \"Fluffy ahead\". Fluffy eh?
You come to a steel door that seems to lead out to the rest of the room.
"""
        text_delay(text)
        raw_input("\nPress ENTER to cautiously open the door --> ")

        text = """You slowly turn the knob and push the steel door open, peering inside.
You notice several large pillars in the room. Then all of a sudden a
huge, red, scaly dragon appears from behind one of the pillars. He aims his head at you.
Immediately a rush of hot air hits you. The heat's unbearable and with your quick reflexes
you slam the door shut. The steel door turns red with heat and you see flames under the door.
\"Fluffy\" eh? Who the fuck labels these doors? You ponder what to do.
"""
        text_delay(text)

        choice = raw_input("\nVisit the merchant before entering? --> ")
        if choice == "yes" or choice == "Yes":
            playdungeon.scenes['merchant'].enter()
            self.door()
        else:
            self.door()

    def door(self):
        text = """\nYou move closer to the door again. It still feels warm to the touch
from the last time you tried to open it. What are you going to do to get through?
"""
        text_delay(text)

        if "lamb meat" in player_inventory.pack_items:
            choice = raw_input("""\n1) Open the door and fuck that dragon up!
2) Push the door open and run as fast as you can to take cover behind a pillar.
3) Push the door open quickly and throw the lamb meat to distract the dragon.
4) Eat the lamb to gain it's strength.
What do you do? -->
""")
            if "1" in choice or "fight" in choice or "fuck" in choice:
                text = """You burst open the door and charge at the dragon.
With one swift breath of the dragon you are instantly vaporized before you take 3 steps. LOL
"""
                text_delay(text)
                game_life.lose_life()
                self.door()
            elif "2" in choice or "run" in choice or "cover" in choice:
                text = """You burst open the door and make a mad dash for the closest pillar.
With one swift breath of the dragon you are instantly vaporized before you take 3 steps. LOL
"""
                text_delay(text)
                game_life.lose_life()
                self.door()
            elif "3" in choice or "lamb" in choice or "cover" in choice:
                text = """You quickly push the door open. Before the dragon can take
another breath to torch your ass you throw the lamb meat as far as you can. The dragon torches
the shit out of it and then chases it down. You take the opportunity to run to the closest pillar.
"""
                text_delay(text)
                self.staircase()
            elif "4" in choice or "eat" in choice or "strength" in choice:
                text = """You take a bite down on the raw lamb leg... You immediately fall violently ill.
"""
                text_delay(text)
                game_life.lose_life()
                self.door()
            else:
                print "Didn't get that, try again."
                self.door()

        else:
            choice = raw_input("""\n1) Open the door and fuck that dragon up!
2) Push the door open and run as fast as you can to take cover behind a pillar.
""")
            if "1" in choice or "fight" in choice or "fuck" in choice:
                text = """You burst open the door and charge at the dragon.
With one swift breath of the dragon you are instantly vaporized before you take 3 steps. LOL
"""
                text_delay(text)
                game_life.lose_life()
                choice = raw_input("Visit the merchant before entering? --> ")
                if choice == "yes" or choice == "Yes":
                    playdungeon.scenes['merchant'].enter()
                    self.door()
                else:
                    self.door()
            elif "2" in choice or "run" in choice or "cover" in choice:
                text = """You burst open the door and make a mad dash for the closest pillar.
With one swift breath of the dragon you are instantly vaporized before you take 3 steps. LOL
"""
                text_delay(text)
                game_life.lose_life()
                choice = raw_input("Visit the merchant before entering? --> ")
                if choice == "yes" or choice == "Yes":
                    playdungeon.scenes['merchant'].enter()
                    self.door()
                else:
                    self.door()
            else:
                print "Didn't get that, please enter again."
                self.door()

    def staircase(self):
        text = """You roll into cover behind the pillar. Catching your breath you hear a loud crunch as the dragon
bites down hard on the scorched lamb meat. Up ahead you see a staircase with the words \"Hostage\"
scribbled above it. That has to be the way. Though the staircase is very exposed and the dragon
is already quiet again, hopefully not knowing where you went. You quickly consider your options.
"""
        text_delay(text)

        if "round shield" in player_inventory.pack_items:
            choice = raw_input("""\n1) Throw your shield as a distraction and run for the staircase.
2) Yell an insult at the dragon and then run.
3) Run as fast as possible and use the shield to guard yourself.
""")
            if "1" in choice or "throw" in choice or "distraction" in choice:
                text = """The shield bangs against the floor away from you and catches the dragon's attention,
unfortunately not for long. As soon as you start to run it spots you makes you the
next hot BBQ item on the dungeon menu.
"""
                text_delay(text)
                game_life.lose_life()
                self.staircase()
            elif "2" in choice or "yell" in choice or "insult" in choice:
                text = """\"DO YOU EVEN LIFT BRO?\" screams from your lungs. You swear
you hear the dragon chuckle as it starts to fly towards you. Before you can
get a few feet from the pillar you have become the dragon's next snack.
"""
                text_delay(text)
                game_life.lose_life()
                self.staircase()

            elif "3" in choice or "guard" in choice:
                text = """You don't skip a beat, sprinting from the pillar toward the staircase.
Immediately the dragon spots you and you see fire spiraling towards you. You
point the shield towards the dragon and continue running. The force of the flame
nearly topples you over and your arm begins to burn, but fuck if this bitch ass dragon
gets between you and that sweet lay tonight. Just a few more steps.......... and you
lower your shoulder as you ram into the door - crashing straight in.
"""
                text_delay(text)
                playthrough.player_move('princess')

#if player does not have shield yet, aka fucked
        else:
            choice = raw_input("""\n1) Run for the staircase.
2) Yell an insult at the dragon and then run.
""")
            if "1" in choice or "run" in choice:
                text = """The dragon spots you instantly and torches your ass.
"""
                text_delay(text)
                game_life.lose_life()
                choice = raw_input("Visit the merchant before entering? --> ")
                if choice == "yes" or choice == "Yes":
                    playdungeon.scenes['merchant'].enter()
                    self.door()
                else:
                    self.door()

            elif "2" in choice or "yell" in choice or "insult" in choice:
                text = """\"DO YOU EVEN LIFT BRO?\" screams from your lungs. You swear
you hear the dragon chuckle as it starts to fly towards you. Before you can
get a few feet from the pillar you have become the dragon's next snack.
"""
                text_delay(text)
                game_life.lose_life()
                choice = raw_input("Visit the merchant before entering? --> ")
                if choice == "yes" or choice == "Yes":
                    playdungeon.scenes['merchant'].enter()
                    self.door()
                else:
                    self.door()
            else:
                print "Didn\'t quite get that. Come again?"
                self.staircase()


#victory, no challenge here
class PrincessRoom(Scene):

    def enter(self):
        text = """\nYou stumble over into the room. Your arm partially burnt, smoke
coming off around you and the stench of burn filling the room. You look up
into the face of a goddess. Blue eyes, blonde hair, supple face. The princess
puts her hand under your chin and pulls you up to one knee. She takes a step back
so that her entire gorgeous body comes into view. She pulls the straps of her dress
over her shoulders and it falls to the ground, exposing all you have worked so hard
for. \"Take me as you will you hunk\" she whispers as she fluffs her brilliant hair behind her back.

            ******* V **********
            ******** I *********
            ******* C **********
            ******** T *********
            ******* O **********
            ******** R *********
            ******* Y **********
"""
        text_delay(text)

        playthrough.roll_credits()


#this is where player items are stored. Called upon to list items with function list_items
class Inventory(object):

    pack_items = ['lucky rabbit\'s tail']

    def list_items(self):
        number_of_items = len(player_inventory.pack_items) #easier way to do this?

        if number_of_items == 0:
            print "\nYour pack is empty. Visit the merchant to stock up."
            global gold
            print "- You have %d gold" % gold
        else:
            print "You currently have the following items in your pack: "
            for item in self.pack_items:
                print "-", item
            global gold
            print "- You have %d gold" % gold


#where players can view available items and purchase using global gold
#purchased items go to pack_items in inventory
class Merchant(Scene):

    menu = {
        'round shield': 75,
        'rope': 50,
        'roses': 50,
        'lamb meat': 25,
        'race guide': 100,
        'extra life': 250}

    def enter(self):
        global gold
        print """\nOy there %s, welcome to the dungeon's black market. You have %d gold.
Please take a look at the menu:
""" % (character_name, gold)
        for item, value in self.menu.iteritems():
            print "*", item, "costs", value, "gold"
        item = raw_input("""What would you like to buy? I'm old and hard of hearing so you need to say it exactly.
Press ENTER for none. -->
""")
        if item in self.menu:
            self.buy(item)
        else:
            print "Could not find item, please try your selection again."
            self.enter

        choice = raw_input("Now would you like to buy something else or leave? --> ")
        if "buy" in choice:
            playdungeon.scenes['merchant'].enter()
        else:
            print "Looking forward to your next gold... er \"visit\" then. Good luck %s!" % character_name


    def buy(self, item):
        cost = self.menu.get(item)
        global gold
        if cost <= gold and item != "extra life":
            player_inventory.pack_items.append(item)
            print "\n%s has been added to your inventory." % item
            gold = gold - cost
            print "You have %d gold remaining." % gold
        elif item == "extra life" and cost <= gold:
            game_life.add_life()
            global lives
            print "You now have %d lives." % lives
            gold = gold - cost
            print "You have %d gold remaining." % gold
        else:
            print "%s, you can't afford that item and I don't believe in charity you peasant." % character_name
            self.enter()


#rooms are stored in dictionary. Used with engine class to proceed through game
class Map(object):
    scenes = {
        'death': Death(),
        'intro': Intro(),
        'merchant': Merchant(),
        'gnomes': GnomeRoom(),
        'race_betting': RacebettingRoom(),
        'darkpool': DarkpoolRoom(),
        'false_princess': FalseprincessRoom(),
        'dragon': DragonRoom(),
        'princess': PrincessRoom()
        }

    def start_scene(self, scene_name):
        scene = Map.scenes.get(scene_name)
        scene.enter()

    def merchant_shop(self):
        self.scenes['merchant'].enter()


#used with map class to proceed through game
class Engine(object):

    feedback = ['Remember, the gorgeous princess is waiting...',
                'Your only shot at love is quickly fading...',
                'You can almost feel the princess\'s breath on your neck...',
                'Will you stay a virgin forever?',
                'Some people were meant to die alone, it\'s okay if you lose.',
                'Your father\'s words echo in your ears... \"Stop looking at me you mistake!\"']


    def player_move(self, next_scene):
        print "\n\n", (random.choice(self.feedback))
        player_move = raw_input("""What do you do now?
1) You can view your current inventory with \"inventory\".
2) You can access the merchant by typing \"merchant\".
3) When you're ready you may proceed with \"press onward\".
What'll it be chump?  ---> """)

        if 'inventory' in player_move or '1' in player_move:
            player_inventory.list_items()
            playthrough.player_move(next_scene)

        elif 'buy' in player_move or 'shop' in player_move or 'merchant' in player_move or '2' in player_move:
            playdungeon.merchant_shop()
            playthrough.player_move(next_scene)

        elif 'press' in player_move or 'onward' in player_move or 'go on' in player_move or 'next' in player_move or '3' in player_move:
            playdungeon.start_scene(next_scene)

        else:
            print "Please try picking again... is it really that hard?"
            playthrough.player_move(next_scene)

    def roll_credits(self):
        print "\n\nCongratulations %s on completing Brave The Dungeon." % character_name
        text = """\n\nBrave the Dungeon was made solely by Aaron Merten when he was
able to keep the bitches at bay and also put his Tinder away.
\nRecognition also goes to Jared Lambert for his expert consultation.
\nBe on the lookout for upcoming products from Mertworks,
packed with even more of what we all want... sex, violence, and more sex.\n\n
"""
        for char in text:
            sys.stdout.write(char)
            time.sleep(0.2)
        sys.exit()


#provides functions for player to lose & add life, death/game over is also implemented here
class Life(object):

    death_feedback = ['Wow you sure messed that one up...',
    'Maybe you want to try that again? After you lose a life though',
    'Were you even trying?',
    'I was right to doubt you when you walked in.',
    'Sorry, there isn\'t an easy mode.']

    def lose_life(self):
        print "\n", (random.choice(self.death_feedback))
        global lives
        lives = lives - 1

        if lives > 1:
            print "You have %s lives left. \nTime seems to rewind..." % lives

        elif lives == 1:
            print "You have %s life left. \nTime seems to rewind..." % lives

        else:
            self.game_over()

    def add_life(self):
        global lives
        lives = lives + 1

    def game_over(self):
        print "\n"
        text = " * * GAME OVER * * "

        for char in text:
            sys.stdout.write(char)
            time.sleep(0.3)
        sys.exit()


#instances to run the game and options to set lives and gold.
game_life = Life()
playcharacter = Character()
player_inventory = Inventory()
playdungeon = Map()
playthrough = Engine()
#starts the game with intro scene, engine and map classes will run the rest
playdungeon.start_scene('intro')
