import random
#Tells you what you and your other should do for the night 
# Should take a list of games and randomly choose one for 
activities = ['Switch/VR', 'Clean Something', 'Do Something Productive', 'Study/Study',  'Watch A Movie!', 'How about some cards\nWhat are you too good for cards?', 'Co-op Switch', 'Take Turns VR', 'Read', 'Solo do what you want', 'Teach Emily Something/Teach Andrew Something', 'Figure it out yourself', 'Flip a coin to decide your next 10 decisions']

switch_games = ['Mario Party w/Teams', 'Mario Party Other', 'Mario Kart', 'Super Smash Bros', 'Civ Rev 6', 'Stardue Valley', 'Lego City Game', 'Lego Incredibles', 'Borderlands 1', 'Borderlands 2', 'Borderlands Other']

def choose_switch_game():
    print("You should play " +random.choice(switch_games))


def what_to_do():
    choice = random.choice(activities)
    print("You two should " + choice)
    if 'witch' in choice:
        choose_switch_game()


what_to_do()

