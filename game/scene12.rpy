define Taylor = Character("Taylor")
define Hayden = Character("Hayden")
define Logan = Character("Logan")
define Bella = Character("Bella")
define Alex = Character("Alex")

label scene12:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    image Taylor = "TaylorPlaceholder.png"
    image Hayden = "HaydenPlaceholder.png"
    image Logan = "LoganPlaceholder.png"
    image Bella = "BellaPlaceholder.png"
    image Alex = "AlexPlaceholder.png"

    show Logan at left
    show Taylor at right:
        zoom 0.65

    Logan "You think we got a spy or some shit?"

    Taylor "Yes. But I don’t know who that spy could be."

    hide Logan
    show Bella at left

    Bella "I mean. If anything, I have been extremely suspicious of Alex the past hour…"

    hide Taylor
    show Alex at right
    
    Alex "What? Why?"

    hide Bella
    show Logan at left

    Logan "I mean. You did kick down the gate to one of the most secure areas in town like it was nothing. It kinda gives off some red flags. Don’t you think?"

    Alex "Come on guys…you two have known me since we were kids! I wouldn’t do anything to hurt you guys! Come on…let’s go take down more of the bad guys! Yeah!"

    show Alex at center
    show Bella at right

    Bella "Yeah! Alex has no reason to be against us! Sure, they did some crazy things but- …but…"

    Alex "Bells, come on…you can trust me! I promise!"

    hide Logan
    show Taylor at left:
        zoom 0.65

    Taylor "Hey Alex…what are your thoughts on us…being here? Taking down the corrupt?"

    Alex "It-it’s fine! Totally just! Totally not illegal! Totally against my values!"

    pause 1.0

    Alex "...Shit"

    hide Bella
    show Hayden at right:
        zoom 0.75

    Hayden "Alex you…"

    Alex "…Welp guess there’s no point in hiding it now."

    hide Taylor
    show Bella at left

    Bella "Alex…what…"

    Alex "You idiots…I was planted undercover in there and I built up your trust. But still…one of you managed to see through it."

    hide Hayden
    show Taylor at right:
        zoom 0.65

    Taylor "I had this…itching feeling. Something felt off in that safehouse. Miss Cara was always in on it, wasn’t she?"

    Alex "Ding ding ding! We lured SO many families into a false sense of security. She felt regret but…I never really did. I got a kick out of it."

    hide Bella
    show Logan at left

    Logan "You bastard…YOU BASTARD…YOU KNOW HOW MANY OF THOSE KIDS JUST WANTED TO GO HOME?!"

    hide Taylor
    show Hayden at right:
        zoom 0.75

    Hayden "Why…why would you do that…?"

    Alex "Immunity to be myself. Why do you think I knew about the gates? Asked for the grenades? Why I was able to kick that stupid gate down?"

    Alex "Immunity. If I do what they say, I get freedom. I’m not letting you ASSHOLES GET IN MY WAY!"

    hide Logan
    show Taylor at left:
        zoom 0.65

    Taylor "What?! SHIT- URGH!"

    Hayden "TAYLOR!"

    Alex "You wanted to get in my way SOOOO badly, Jenkins. Why? Why get in my way when you KNOW there is a bounty on YOUR HEAD?!"

    Taylor "I don’t just stand alone for myself, but for EVERYONE THAT DESERVES TO BE FREED! HAAAAA!"

    label test_menu2:

    $ tries = 5
    $ wins = 0

    $ import random

    # Start battle loop
    label battle_loop2:

    if tries <= 0:
        jump check_result2

    menu:
        "Choose your move:"

        "Strike":
            # 80% chance to succeed
            $ result = 1 if random.random() < 0.8 else 0

        "Defend":
            # 50% chance to succeed
            $ result = 1 if random.random() < 0.5 else 0

        "Counter":
            # 30% chance to succeed
            $ result = 1 if random.random() < 0.8 else 0

    if result == 1:
        $ wins += 1
        "You gained the advantage!"
    else:
        "Alex gained the advantage!"

    $ tries -= 1

    "Wins: [wins] / 5   Tries left: [tries]"

    jump battle_loop2  # repeat the loop

# Check result after all tries
label check_result2:

    if wins >= 4:
        jump alex_defeat
    else:
        jump alex_win

# BAD END
label alex_win:

    show Alex at center

    Alex "Not so tough now, are you Jenkins?"

    scene black with fade

    "GAME END"

    jump scene12

# GOOD END (YOU WIN)

label alex_defeat:

    show Alex at center

    Alex "URGH…DAMMIT…YOU…URGH…"

    return

